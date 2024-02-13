import os
import shutil
import json
import time

def reformat_json(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extraire la clé et la valeur de l'objet JSON
        key, value = next(iter(data.items()))

        # Analyse de la clé JSON pour extraire les valeurs
        json_key = json.loads(key.replace("\\", "").strip('"'))

        # Créer un nouveau dictionnaire avec les informations extraites
        reformatted_data = {
            "mediaType": json_key.get("mediaType", ""),
            "boolMediaMultipleSeason": json_key.get("boolMediaMultipleSeason", False),
            "boolAlreadyExist": json_key.get("boolAlreadyExist", False),
            "NameMedia": json_key.get("NameMedia", "")
        }
        
        # Écrire les données reformatées dans le fichier d'entrée
        with open(input_file, 'w', encoding='utf-8') as f:
            json.dump(reformatted_data, f, ensure_ascii=False, indent=2)
        
        print("Fichier JSON reformaté avec succès.")
    
    except FileNotFoundError:
        print(f"Erreur: Le fichier {input_file} n'existe pas.")
    except json.JSONDecodeError:
        print(f"Erreur: Impossible de décoder le fichier JSON {input_file}.")
    except (ValueError, SyntaxError):
        print("Erreur: Le format du fichier JSON est incorrect.")

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
    reformat_json(jsonFile)
    try:
        # Attendre quelques secondes pour voir si le fichier est disponible
        time.sleep(1)
        
        with open(jsonFile, 'r', encoding='utf-8') as f:
            data = json.load(f)
            nameMedia = data.get('NameMedia')
            if nameMedia:
                mediaPath = os.path.join(mediaDir, nameMedia.encode('utf-8').decode('latin1'))
                os.makedirs(mediaPath, exist_ok=True)
                # Déplace le json dans le cas où l'utilisateur a besoin du Json dans son fichier téléchargé
                shutil.move(jsonFile, mediaPath)
                return nameMedia
            else:
                print("Erreur: 'NameMedia' n'est pas spécifié dans le fichier JSON.")
                return None
    except PermissionError:
        print(f"Erreur: Impossible de déplacer ou de supprimer le fichier {jsonFile} car il est utilisé par un autre processus.")
        return nameMedia
    except FileNotFoundError as e:
        print(f"Erreur: {e.strerror} ({e.filename})")
        return None
    except json.JSONDecodeError:
        print(f"Erreur: Impossible de décoder le fichier JSON {jsonFile}.")
        return None

def torrentAndJsonManagementMain():
    configDir = 'config'
    configJson = os.path.join(configDir, 'path.json')
    paths = loadPathsFromJson(configJson)
    
    if paths is not None:
        sourceDirJson = paths.get('sourceDirJson')
        sourceDirTorrent = paths.get('sourceDirTorrent')
        targetDir = paths.get('mediaDir')
        inputDirDeluge = paths.get('inputDirDeluge')
        
        fileTorrent, jsonFile = checkDuplicateFiles(sourceDirJson, sourceDirTorrent, inputDirDeluge)
        if fileTorrent:
            moveTorrentToDeluge(sourceDirTorrent, fileTorrent, inputDirDeluge)
            if jsonFile:
                nameMedia = createMediaDirFromJson(targetDir, jsonFile)
                # print ("Manage Torrent and Json, nameMedia:",nameMedia)
                return fileTorrent, nameMedia  # Retourne le nom du torrent et le nom du média
    else:
        return None, None  # Si les chemins ne sont pas chargés correctement
