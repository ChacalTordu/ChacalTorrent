import os
import json

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
        print(f"Erreur: Le fichier {file_inputJson} n'existe pas.")
    except json.JSONDecodeError:
        print(f"Erreur: Impossible de décoder le fichier JSON {file_inputJson}.")
    except (ValueError, SyntaxError):
        print("Erreur: Le format du fichier JSON est incorrect.")

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
            # shutil.move(file_jsonFile, mediaPath)     # Move the JSON if needed
            print(f"[OK] : Création du dossier {nameMedia} dans {path_newMediaDir} est réalisé avec succés")
            return None
        else:
            return None, "Error: 'NameMedia' is not specified in the JSON file."
    except PermissionError as e:
        return None, f"Error: Unable to move or delete the file {file_jsonFile} as it is being used by another process. ({str(e)})"
    except FileNotFoundError as e:
        return None, f"Error: {e.strerror} ({e.filename})"
    except json.JSONDecodeError:
        return None, f"Error: Unable to decode the JSON file {file_jsonFile}."


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
        print(f"Error: The file {file_jsonData} does not exist.")
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
        print(f"Error: The file {file_jsonData} does not exist.")
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
        print(f"Error: The file {file_jsonData} does not exist.")
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
        print(f"Error: The file {file_jsonData} does not exist.")
        return ""
