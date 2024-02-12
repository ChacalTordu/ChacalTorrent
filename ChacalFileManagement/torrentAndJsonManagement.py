import os
import shutil
import json

def loadPathsFromJson(jsonFile):
    try:
        with open(jsonFile, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Erreur: Le fichier {jsonFile} n'existe pas.")
        return None
    except json.JSONDecodeError:
        print(f"Erreur: Impossible de décoder le fichier JSON {jsonFile}.")
        return None

def checkDuplicateFiles(sourceDirJson, sourceDirTorrent, inputDirDeluge):
    try:
        filesJson = set(os.listdir(sourceDirJson))
        filesTorrent = set(os.listdir(sourceDirTorrent))
        
        for fileJson in filesJson:
            nameJson = os.path.splitext(fileJson)[0]  # Retire l'extension .json
            for fileTorrent in filesTorrent:
                nameTorrent = os.path.splitext(fileTorrent)[0]  # Retire l'extension .torrent
                if nameJson == nameTorrent:
                    # print("Fichier à télécharger:", nameJson)
                    return fileTorrent, os.path.join(sourceDirJson, fileJson)  # Renvoie le nom du fichier torrent et le fichier JSON correspondant
        return None, None  # Si aucun fichier en double n'est trouvé
    except FileNotFoundError as e:
        print(f"Erreur: {e.strerror} ({e.filename})")
        return None, None

def moveTorrentToDeluge(sourceDirTorrent, fileTorrent, inputDirDeluge):
    try:
        sourcePath = os.path.join(sourceDirTorrent, fileTorrent)
        targetPath = os.path.join(inputDirDeluge, fileTorrent)
        shutil.move(sourcePath, targetPath)
    except FileNotFoundError as e:
        print(f"Erreur: {e.strerror} ({e.filename})")

def createMediaDirFromJson(mediaDir, jsonFile):
    try:
        with open(jsonFile, 'r') as f:
            data = json.load(f)
            nameMedia = data.get('NameMedia')
            if nameMedia:
                mediaPath = os.path.join(mediaDir, nameMedia)
                os.makedirs(mediaPath, exist_ok=True)
                # Déplacez le fichier JSON dans le dossier créé
                shutil.move(jsonFile, mediaPath)
                # Supprimez le fichier JSON du dossier source
                os.remove(jsonFile)
            else:
                print("Erreur: 'NameMedia' n'est pas spécifié dans le fichier JSON.")
    except PermissionError:
        print(f"Erreur: Impossible de déplacer ou de supprimer le fichier {jsonFile} car il est utilisé par un autre processus.")
    except FileNotFoundError as e:
        print(f"Erreur: {e.strerror} ({e.filename})")
    except json.JSONDecodeError:
        print(f"Erreur: Impossible de décoder le fichier JSON {jsonFile}.")

def manageTorrentAndJson():
    # Load paths from configuration JSON
    configDir = 'config'
    configJson = os.path.join(configDir, 'path.json')
    paths = loadPathsFromJson(configJson)
    
    if paths is not None:
        sourceDirJson = paths.get('sourceDirJson')
        sourceDirTorrent = paths.get('sourceDirTorrent')
        targetDir = paths.get('mediaDir')
        inputDirDeluge = paths.get('inputDirDeluge')
        
        # Check for duplicate files
        fileTorrent, jsonFile = checkDuplicateFiles(sourceDirJson, sourceDirTorrent, inputDirDeluge)
        if fileTorrent:
            moveTorrentToDeluge(sourceDirTorrent, fileTorrent, inputDirDeluge)
            if jsonFile:
                createMediaDirFromJson(targetDir, jsonFile)

if __name__ == "__main__":
    manageTorrentAndJson()