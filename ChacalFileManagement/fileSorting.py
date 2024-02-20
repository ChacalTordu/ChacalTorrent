import os
import shutil

import common

def checkValidateParameter(path_outputDirDeluge, path_newDirMedia, fileJson):
    """
    Vérifie la validité des paramètres.
    
    Vérifie si le fichier JSON n'est pas vide, si le dossier de sortie Deluge existe et si le nouveau dossier média existe.
    """
    if not fileJson:
        raise ValueError("Fichier JSON vide")

    if not os.path.exists(path_outputDirDeluge):
        raise FileNotFoundError(f"Le dossier de recherche {path_outputDirDeluge} n'existe pas.")

    if not os.path.exists(path_newDirMedia):
        raise FileNotFoundError(f"Le dossier des nouveaux médias {path_newDirMedia} n'existe pas.")

def checkMatchingFiles(path_outputDirDeluge, file_listNameFileSought):
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
                pathTarget = os.path.join(path_outputDirDeluge, baseName, name)
                try:
                    shutil.move(pathSource, pathTarget)
                    print(f"[OK] : {name} déplacé avec succès vers {pathTarget}.")
                except Exception as e:
                    print(f"[ERR] Erreur lors du déplacement de {name} : {str(e)}\n[INFOS] : pathTarget = {pathTarget}\n[INFOS] : pathSource = {pathSource}")
            # else:
            #     print(f"Recherche du fichier téléchargé :\n{baseName} n'est pas dans la liste des noms à correspondre.")


def createNewFileSought(path_newDirMedia, file_json):
    """
    Crée un nouveau média à chercher.

    Args:
        path_newDirMedia (str): Le chemin du dossier où créer les médias.
        file_json (str): Le chemin du fichier JSON.

    Returns:
        str: Le chemin complet du fichier de la liste des fichiers recherchés.
    """
    common.createMediaDirFromJson(path_newDirMedia, file_json) # Creation of mediaDir

    list_nameFileSought_file = os.path.join(path_newDirMedia, "listFileSought")
    nameFileSought = os.path.splitext(os.path.basename(file_json))[0]

    try:
        if os.path.exists(list_nameFileSought_file):
            with open(list_nameFileSought_file, 'a') as f:
                f.write(nameFileSought + '\n')
        else:
            with open(list_nameFileSought_file, 'w') as f:
                f.write(nameFileSought + '\n')

        print(f"[OK] : Création du nouvel élément {nameFileSought} dans la liste de recherche ")
        return list_nameFileSought_file
    except Exception as e:
        return {str(e)}


def fileSortingMain(path_outputDirDeluge, path_newDirMedia, file_json):
    """
    Fonction principale pour trier les fichiers.
    
    Coordonne le processus de tri des fichiers en appelant les fonctions auxiliaires.
    """
    try:
        checkValidateParameter(path_outputDirDeluge, path_newDirMedia, file_json)       # Check parameter
        file_listNameFileSought = createNewFileSought(path_newDirMedia, file_json)      # Create list of seek nameMedia
        checkMatchingFiles(path_outputDirDeluge, file_listNameFileSought)               # Check matching newmedia depends on seekNameMedia
    except (ValueError, FileNotFoundError) as e:
        return str(e)
    except Exception as e:
        return str(e)
