import os
import shutil

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
            # Vérifier si le nom de base correspond à l'un des noms recherchés
            if baseName in list_nameFileSought:
                pathSource = os.path.join(root, name)
                pathTarget = os.path.join(path_newDirMedia, baseName, name) 
                try:
                    shutil.move(pathSource, pathTarget)
                    print(f"[OK] : {name} déplacé avec succès vers {pathTarget}.")
                    pathTarget = os.path.dirname(pathTarget)
                    common.renameDirectory(pathTarget) # Rename folder 
                    return name
                except Exception as e:
                    raise Exception(f"[ERR] Erreur lors du déplacement de {name} : {str(e)}\n[INFOS] : pathSource = {pathSource}\n[INFOS] : pathTarget = {pathTarget}")
    return None

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

        print(f"[OK] : Attente de fin de téléchargement de {nameFileSought} ... ")
        return file_listNameFileSought
    except Exception as e:
        raise Exception(f"{str(e)}")

def fileSortingMain(path_outputDirDeluge, path_newDirMedia, file_json, file_listNameFileSought):
    """
    Fonction principale pour trier les fichiers.
    
    Coordonne le processus de tri des fichiers en appelant les fonctions auxiliaires.
    """
    try:
        if file_json is not None:
            checkValidateParameter(path_outputDirDeluge, path_newDirMedia, file_json, file_listNameFileSought)          # Check parameter
            createNewFileSought(path_newDirMedia, file_json)                                                            # Create list of seek nameMedia
        nameMediaDownloaded = checkMatchingFiles(path_newDirMedia, path_outputDirDeluge, file_listNameFileSought)       # Check matching newmedia depends on seekNameMedia
        return nameMediaDownloaded
    except (ValueError, FileNotFoundError) as e:
        raise ValueError(f"{str(e)}")
    except Exception as e:
        raise Exception(f"{str(e)}")
