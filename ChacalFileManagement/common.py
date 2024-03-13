import os
import json
import shutil
import logging

from logger_config import logger

def getMediaDirectories(path_json):
    """
    Retrieve media directories paths from a JSON file.

    Args:
        json_file_path (str): The path to the JSON file.

    Returns:
        dict: A dictionary containing the paths of media directories.
    """
    try:
        with open(path_json, 'r') as file:
            data = json.load(file)
            path_mediaDirectories = {
                "path_mediaDirMovie": data.get("path_mediaDirMovie"),
                "path_mediaDirCartoon": data.get("path_mediaDirCartoon"),
                "path_mediaDirShows": data.get("path_mediaDirShows"),
                "path_mediaDirAnime": data.get("path_mediaDirAnime")
            }
            return path_mediaDirectories
    except FileNotFoundError as e:
        raise FileNotFoundError(f"{e}")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"{e}")

def loadPaths(jsonFile):
    """
    Charge les chemins à partir du fichier JSON spécifié.

    Args:
        jsonFile (str): Chemin vers le fichier JSON contenant les chemins.

    Returns:
        tuple: Un tuple contenant les chemins (pathSourceDirJson, pathSourceDirTorrent, newDirMedia, pathInputDirDeluge, pathOutputDirDeluge, pathNewDirMedia, error)
    """
    logger = logging.getLogger(__name__)

    try:
        if not os.path.exists(jsonFile):
            logger.error(f"Erreur: Le fichier {jsonFile} n'existe pas.")
            return None, None, None, None, None, f"Erreur: Le fichier {jsonFile} n'existe pas."
        else:
            with open(jsonFile, 'r') as f:
                data = json.load(f)
            
            if data is not None:
                pathSourceDirJson = data.get('path_sourceDirJson')
                pathSourceDirTorrent = data.get('path_sourceDirTorrent')
                pathInputDirDeluge = data.get('path_inputDirDeluge')
                pathOutputDirDeluge = data.get('path_outputDirDeluge')
                pathNewDirMedia = data.get('path_mediaDir')

                # Créer le dossier s'il n'existe pas
                if pathNewDirMedia and not os.path.exists(pathNewDirMedia):
                    os.makedirs(pathNewDirMedia)

                return pathSourceDirJson, pathSourceDirTorrent, pathInputDirDeluge, pathOutputDirDeluge, pathNewDirMedia, None
            else:
                logger.error(f"Erreur: Le fichier {jsonFile} est vide.")
                return None, None, None, None, None, f"Erreur: Le fichier {jsonFile} est vide."
    except FileNotFoundError:
        logger.error(f"Erreur: Le fichier {jsonFile} n'existe pas.")
        return None, None, None, None, None, f"Erreur: Le fichier {jsonFile} n'existe pas."
    except json.JSONDecodeError:
        logger.error(f"Erreur: Impossible de décoder le fichier JSON {jsonFile}.")
        return None, None, None, None, None, f"Erreur: Impossible de décoder le fichier JSON {jsonFile}."
    except Exception as e:
        logger.error(f"Une erreur s'est produite lors du chargement des chemins à partir du fichier JSON : {str(e)}")
        return None, None, None, None, None, f"Une erreur s'est produite lors du chargement des chemins à partir du fichier JSON : {str(e)}"

def reformatJson(file_inputJson):
    """
    Reformate un fichier JSON en modifiant sa structure.

    Args:
        input_file (str): Chemin vers le fichier JSON à reformater.

    Raises:
        FileNotFoundError: Si le fichier spécifié n'existe pas.
        json.JSONDecodeError: Si le fichier JSON ne peut pas être décodé.
        ValueError: Si le format du fichier JSON est incorrect.
        SyntaxError: Si une erreur de syntaxe se produit lors du reformatage du fichier JSON.
    """
    try:
        with open(file_inputJson, 'r', encoding='utf-8') as f:
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
        with open(file_inputJson, 'w', encoding='utf-8') as f:
            json.dump(reformatted_data, f, ensure_ascii=False, indent=2)
    
    except FileNotFoundError:
        logger.error(f"Erreur: Le fichier {file_inputJson} n'existe pas.")
    except json.JSONDecodeError:
        logger.error(f"Erreur: Impossible de décoder le fichier JSON {file_inputJson}.")
    except (ValueError, SyntaxError):
        logger.error("Erreur: Le format du fichier JSON est incorrect.")

def renameDirectory(path_dir):
    """
    Rename a directory.

    Args:
        path_dir (str): The path to the directory to be renamed.

    Returns:
        str: The new path of the renamed directory.
    """
    try:
        # Obtenez le nom du dossier
        dir_name = os.path.basename(path_dir)
        # Obtenez le chemin du fichier JSON
        file_jsonData = os.path.join(path_dir, f"{dir_name}.json")
        # Remplacer les barres obliques inverses par des barres obliques normales
        file_jsonData = os.path.normpath(file_jsonData)
        new_name = getNameMediaFromJson(file_jsonData)

        if not new_name:
            logger.error(f"[ERR]: Cannot rename directory. Metadata not found or invalid in {file_jsonData}")
            return None

        # Obtenir le chemin du répertoire parent
        path_parent = os.path.dirname(path_dir)
        # Construire le nouveau chemin complet avec le nouveau nom
        path_newDirectory = os.path.join(path_parent, new_name)
        # Renommer le répertoire
        os.rename(path_dir, path_newDirectory)
        logger.info(f"[OK] : Le dossier a été renommé avec succès en '{new_name}'.")
        return path_newDirectory, new_name
    except Exception as e:
        logger.error(f"[ERR] Error occurred while renaming directory: {str(e)}")
        return None


def createMediaDirFromJson(path_newMediaDir, file_jsonFile):
    """
    Create a media directory based on information from a JSON file.

    Args:
        path_newMediaDir (str): Path to the directory where to create the media directory.
        file_jsonFile (str): Path to the JSON file containing information about the media.

    Returns:
        str or None: The name of the created media, or an error message in case of failure.
    """
    try:
        reformatJson(file_jsonFile)
        # nameMedia = getNameMediaFromJson(file_jsonFile)
        nameMedia = os.path.splitext(os.path.basename(file_jsonFile))[0]
        if nameMedia:
            mediaPath = os.path.join(path_newMediaDir, nameMedia.encode('utf-8').decode('latin1'))
            os.makedirs(mediaPath, exist_ok=True)       # Create the directory
            shutil.move(file_jsonFile, mediaPath)       # Move the JSON in it
            logger.info(f"[OK] : Création du dossier {nameMedia} dans {path_newMediaDir} est réalisé avec succés")
            return None
        else:
            return None, "[ERR] : 'NameMedia' is not specified in the JSON file."
    except PermissionError as e:
        return None, f"[ERR] : Unable to move or delete the file {file_jsonFile} as it is being used by another process. ({str(e)})"
    except FileNotFoundError as e:
        return None, f"[ERR] : {e.strerror} ({e.filename})"
    except json.JSONDecodeError:
        return None, f"[ERR] : Unable to decode the JSON file {file_jsonFile}."


def getMediaTypeFromJson(file_jsonData):
    """
    Retrieves the media type from JSON data.

    Args:
        file_jsonData (str): Path to the JSON file.

    Returns:
        str: The media type.
    """
    try:
        with open(file_jsonData, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('mediaType')
    except FileNotFoundError:
        logger.error(f"[ERR] : The file {file_jsonData} does not exist.")
        return ""

def getBoolMediaMultipleSeasonFromJson(file_jsonData):
    """
    Retrieves the boolean indicating whether the media has multiple seasons from JSON data.

    Args:
        file_jsonData (str): Path to the JSON file.

    Returns:
        bool: True if the media has multiple seasons, False otherwise.
    """
    try:
        with open(file_jsonData, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('boolMediaMultipleSeason')
    except FileNotFoundError:
        logger.error(f"[ERR] : The file {file_jsonData} does not exist.")
        return False

def getBoolAlreadyExistFromJson(file_jsonData):
    """
    Retrieves the boolean indicating whether the media already exists from JSON data.

    Args:
        file_jsonData (str): Path to the JSON file.

    Returns:
        bool: True if the media already exists, False otherwise.
    """
    try:
        with open(file_jsonData, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('boolAlreadyExist')
    except FileNotFoundError:
        logger.error(f"[ERR] : The file {file_jsonData} does not exist.")
        return False

def getNameMediaFromJson(file_jsonData):
    """
    Retrieves the name of the media from JSON data.

    Args:
        file_jsonData (str): Path to the JSON file.

    Returns:
        str: The name of the media.
    """
    try:
        with open(file_jsonData, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('NameMedia')
    except FileNotFoundError:
        logger.error(f"[ERR] : The file {file_jsonData} does not exist.")
        return ""
