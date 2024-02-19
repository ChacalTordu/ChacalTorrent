import os
import shutil

# def renameFile(targetDir, oldName, newName):
#     try:
#         # Construire le chemin complet de l'ancien nom de fichier
#         oldFilePath = os.path.join(targetDir, oldName)
        
#         # Extraire l'extension de l'ancien nom de fichier
#         _, extension = os.path.splitext(oldName)
        
#         # Construire le chemin complet du nouveau nom de fichier avec extension
#         # Récupérer le nouveau nom depuis le dossier
#         newNameFromFolder = os.path.join(targetDir, newName, oldName)
#         newFilePath = os.path.join(targetDir, newName, newName + extension)
        
#         # Renommer le fichier
#         os.rename(newNameFromFolder, newFilePath)
#         print(f"Le fichier {oldName} a été renommé en {newName + extension}.")
#     except FileNotFoundError as e:
#         print(f"Erreur lors du renommage du fichier : {str(e)}")
#     except Exception as e:
#         print(f"Une erreur s'est produite lors du renommage du fichier : {str(e)}")

def fileSortingMain(path_outputDirDeluge, path_newDirMedia, file_json):
    try:
        if not file_json:
            nameFileSought, _ = os.path.splitext(file_json)
            raise print(f"[ERR] : Fichier json vide")
        # Vérifier si le dossier de recherche existe
        if not os.path.exists(path_outputDirDeluge):
            raise FileNotFoundError(f"[ERR] : Le dossier de recherche {path_outputDirDeluge} n'existe pas.")
        # Vérifier si le dossier du nouveau media existe
        if not os.path.exists(path_newDirMedia):
            raise FileNotFoundError(f"[ERR] : Le dossier du nouveau média {path_newDirMedia} n'existe pas.")
        
        # Parcourir les fichiers et dossiers dans le dossier cible
        for root, dirs, files in os.walk(path_outputDirDeluge):
            for name in files + dirs:
                # Extraire le nom de fichier sans extension
                baseName, _ = os.path.splitext(name)
                if baseName == nameFileSought:
                    # Construire les chemins source et cible
                    path_source = os.path.join(root, name)
                    path_target = os.path.join(path_outputDirDeluge, nameFileSought, name)
                    try:
                        # Déplacer le fichier/dossier vers le dossier créé par createMediaDirFromJson
                        shutil.move(path_source, nameFileSought)
                        print(f"[OK] : {name} déplacé avec succès vers {path_target}.")
                    except Exception as e:
                        print(f"[ERR] : Erreur lors du déplacement de {name} : {str(e)}")
    except FileNotFoundError as e:
        print(f"[ERR] : Erreur dans fileSortingMain: {str(e)}")
    except Exception as e:
        print(f"[ERR] : Une erreur s'est produite dans fileSortingMain: {str(e)}")

