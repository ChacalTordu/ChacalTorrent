import os
import shutil
import json

from logger_config import logger
import common

def checkValidateParameter(path_outputDirDeluge, path_newDirMedia, fileJson, file_listNameFileSought):
    """
    Vérifie la validité des paramètres.
    
    Vérifie si le fichier JSON n'est pas vide, si le dossier de sortie Deluge existe et si le nouveau dossier média existe.
    """
    if not fileJson:
        raise ValueError("Fichier JSON vide")

    if not os.path.exists(path_outputDirDeluge):
        raise FileNotFoundError(f"Le dossier outputDirDeluge {path_outputDirDeluge} n'existe pas.")

    if not os.path.exists(path_newDirMedia):
        raise FileNotFoundError(f"Le dossier des nouveaux médias {path_newDirMedia} n'existe pas.")
    
    if not os.path.exists(file_listNameFileSought):
        raise FileNotFoundError(f"Le fichier de recherche {file_listNameFileSought} n'existe pas.")
    
def checkMatchingFiles(path_newDirMedia, path_outputDirDeluge, file_listNameFileSought):
    """
    Déplace les fichiers/dossier qui match avec l'un des noms de la file_listNameFileSought vers le dossier média correspondant.
    
    Parcourt les fichiers dans le dossier de sortie Deluge et déplace ceux correspondant au nom recherché vers le nouveau dossier média.
    """

    with open(file_listNameFileSought, 'r') as f:
        list_nameFileSought = f.read().splitlines()

    for root, dirs, files in os.walk(path_outputDirDeluge):
        for name in files + dirs:
            baseName, _ = os.path.splitext(name)
            if baseName in list_nameFileSought:
                pathSource = os.path.join(root, name)
                pathTarget = os.path.join(path_newDirMedia, baseName, name) 
                try:
                    shutil.move(pathSource, pathTarget)
                    logger.info(f"[OK] : {name} déplacé avec succès vers {pathTarget}.")
                    list_nameFileSought.remove(baseName)
                    with open(file_listNameFileSought, 'w') as file:
                        file.write('\n'.join(list_nameFileSought))
                    pathTarget = os.path.dirname(pathTarget)
                    path_newDir, newName = common.renameDirectory(pathTarget)
                    return newName, path_newDir
                except Exception as e:
                    raise Exception(f"[ERR] Erreur lors du déplacement de {name} : {str(e)}\n[INFOS] : pathSource = {pathSource}\n[INFOS] : pathTarget = {pathTarget}")
    return None, None

def createNewFileSought(path_newDirMedia, file_json):
    """
    Crée un nouveau média à chercher.

    Args:
        path_newDirMedia (str): Le chemin du dossier où créer les médias.
        file_json (str): Le chemin du fichier JSON.

    Returns:
        str: Le chemin complet du fichier de la liste des fichiers recherchés.
    """
    common.createMediaDirFromJson(path_newDirMedia, file_json) # Creation of mediaDir w/ json in it

    file_listNameFileSought = os.path.join(path_newDirMedia, "listFileSought")

    nameFileSought = os.path.splitext(os.path.basename(file_json))[0]

    try:
        if os.path.exists(file_listNameFileSought):
            # Vérifier si le nom est déjà présent dans le fichier
            with open(file_listNameFileSought, 'r') as f:
                existing_names = f.read().splitlines()
            if nameFileSought not in existing_names:
                # Si le nom n'est pas déjà présent, l'ajouter
                with open(file_listNameFileSought, 'a') as f:
                    f.write(nameFileSought + '\n')
        else:
            with open(file_listNameFileSought, 'w') as f:
                f.write(nameFileSought + '\n')

        logger.info(f"[OK] : Attente de fin de téléchargement de {nameFileSought} ... ")
        return file_listNameFileSought
    except Exception as e:
        raise Exception(f"{str(e)}")
    
def getFinalPath(path_newDirTarget):
    """
    Get the final path for moving the directory based on the media type.

    Returns:
        str: The final path for moving the directory.
    """
    try:
        path_json = os.path.join(os.path.dirname(__file__), "../config", "config.json") # Load json file
        media_directories = common.getMediaDirectories(path_json) # Load path from json
        
        # Obtenez la liste des fichiers dans le répertoire cible
        files_in_dir = os.listdir(path_newDirTarget)
        
        # Recherchez le premier fichier JSON dans la liste des fichiers
        json_file = None
        for file_name in files_in_dir:
            if file_name.endswith('.json'):
                json_file = os.path.join(path_newDirTarget, file_name)
                break
        
        # Vérifiez si un fichier JSON a été trouvé
        if json_file is None:
            raise FileNotFoundError("No JSON file found in directory.")
        
        # Obtenez le type de média du fichier JSON
        media = common.getMediaTypeFromJson(json_file)
        
        # Obtenez le chemin final en fonction du type de média
        if media == "Movie":
            final_path = media_directories["path_mediaDirMovie"]
        elif media == "Cartoon":
            final_path = media_directories["path_mediaDirCartoon"]
        elif media == "Shows":
            final_path = media_directories["path_mediaDirShows"]
        elif media == "Anime":
            final_path = media_directories["path_mediaDirAnime"]
        else:
            raise ValueError(f"Unknown media type: {media}")
        
        return final_path
    
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise Exception(f"Error while getting final path: {str(e)}")

def fileSortingMain(path_outputDirDeluge, path_newDirMedia, file_json, file_listNameFileSought):
    """
    Fonction principale pour trier les fichiers.
    
    Coordonne le processus de tri des fichiers en appelant les fonctions auxiliaires.
    """
    try:
        if file_json is not None:
            checkValidateParameter(path_outputDirDeluge, path_newDirMedia, file_json, file_listNameFileSought)                          # Check parameter
            createNewFileSought(path_newDirMedia, file_json)                                                                            # Create list of seek nameMedia
        nameMediaDownloaded, path_newDir = checkMatchingFiles(path_newDirMedia, path_outputDirDeluge, file_listNameFileSought)          # Check matching newmedia depends on seekNameMedia
        if path_newDir is not None:
            # print(f"Fichier téléchargé\nPath source: {path_newDir}\nPath Target: {getFinalPath(path_newDir)}")
            shutil.move(path_newDir,getFinalPath(path_newDir))                                                                          # Move the final folder into the good one                                                                                  
        return nameMediaDownloaded
    except (ValueError, FileNotFoundError) as e:
        raise ValueError(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")
