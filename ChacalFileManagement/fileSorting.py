import os
import shutil

def renameFile(targetDir, oldName, newName):
    try:
        # Construire le chemin complet de l'ancien nom de fichier
        oldFilePath = os.path.join(targetDir, oldName)
        
        # Extraire l'extension de l'ancien nom de fichier
        _, extension = os.path.splitext(oldName)
        
        # Construire le chemin complet du nouveau nom de fichier avec extension
        # Récupérer le nouveau nom depuis le dossier
        newNameFromFolder = os.path.join(targetDir, newName, oldName)
        newFilePath = os.path.join(targetDir, newName, newName + extension)
        
        # Renommer le fichier
        os.rename(newNameFromFolder, newFilePath)
        print(f"Le fichier {oldName} a été renommé en {newName + extension}.")
    except FileNotFoundError as e:
        print(f"Erreur lors du renommage du fichier : {str(e)}")
    except Exception as e:
        print(f"Une erreur s'est produite lors du renommage du fichier : {str(e)}")


def fileOrFolderScanner(targetDir, torrentName, nameMedia):
    try:
        # Vérifier si le dossier cible existe
        if not os.path.exists(targetDir):
            raise FileNotFoundError(f"Le dossier cible {targetDir} n'existe pas.")
        
        # Parcourir les fichiers et dossiers dans le dossier cible
        for root, dirs, files in os.walk(targetDir):
            for name in files + dirs:
                # Extraire le nom de fichier sans extension
                base_name, _ = os.path.splitext(name)
                if base_name == torrentName:
                    # Construire les chemins source et cible
                    sourcePath = os.path.join(root, name)
                    targetPath = os.path.join(targetDir, torrentName, name)
                    try:
                        # Déplacer le fichier/dossier vers le dossier créé par createMediaDirFromJson
                        shutil.move(sourcePath,nameMedia)
                        print(f"{name} déplacé avec succès vers {targetPath}.")
                    except Exception as e:
                        print(f"Erreur lors du déplacement de {name} : {str(e)}")
                else : 
                    print("Erreur dans fileSorting, base_name != torrentName\nbase_Name: ",base_name,"\nnameMedia: ",nameMedia)
    
    except FileNotFoundError as e:
        print(f"Erreur dans fileSorting: {str(e)}")
    except Exception as e:
        print(f"Une erreur s'est produite dans fileSorting: {str(e)}")

def fileSortingMain(targetDir, torrentName, nameMedia):
    try:
        # Appeler fileOrFolderScanner pour déplacer le fichier
        fileOrFolderScanner(targetDir, torrentName, nameMedia)
    except FileNotFoundError as e:
        print(f"Erreur dans fileSortingMain: {str(e)}")
    except Exception as e:
        print(f"Une erreur s'est produite dans fileSortingMain: {str(e)}")

