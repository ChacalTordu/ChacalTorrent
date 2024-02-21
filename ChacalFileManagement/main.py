import os
import json
import signal
import multiprocessing
import logging

import torrentAndJsonManagement
import fileSorting

def configure_logging():
    """
    Configure le logging pour écrire les messages dans un fichier.
    """
    # Création d'un logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Création d'un formateur pour formater les messages
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Création d'un handler pour écrire dans un fichier
    file_handler = logging.FileHandler('fileManagement.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Ajout du handler au logger
    logger.addHandler(file_handler)

def loadPaths(jsonFile):
    """
    Charge les chemins à partir du fichier JSON spécifié.

    Args:
        jsonFile (str): Chemin vers le fichier JSON contenant les chemins.

    Returns:
        tuple: Un tuple contenant les chemins (pathSourceDirJson, pathSourceDirTorrent, newDirMedia, pathInputDirDeluge, pathOutputDirDeluge, pathNewDirMedia, error)
    """
    try:
        if not os.path.exists(jsonFile):
            logging.error(f"Le fichier {jsonFile} n'existe pas.")
            return None, None, None, None, None, None, f"Erreur: Le fichier {jsonFile} n'existe pas."
        else:
            with open(jsonFile, 'r') as f:
                data = json.load(f)
            if data is not None:
                pathSourceDirJson = data.get('sourceDirJson')
                pathSourceDirTorrent = data.get('sourceDirTorrent')
                pathInputDirDeluge = data.get('inputDirDeluge')
                pathOutputDirDeluge = data.get('outputDirDeluge')
                pathNewDirMedia = data.get('mediaDir')
                return pathSourceDirJson, pathSourceDirTorrent, pathInputDirDeluge, pathOutputDirDeluge, pathNewDirMedia, None
            else:
                logging.error(f"Le fichier {jsonFile} est vide.")
                return None, None, None, None, None, f"Erreur: Le fichier {jsonFile} est vide."
    except FileNotFoundError:
        logging.error(f"Le fichier {jsonFile} n'existe pas.")
        return None, None, None, None, None, f"Erreur: Le fichier {jsonFile} n'existe pas."
    except json.JSONDecodeError:
        logging.error(f"Impossible de décoder le fichier JSON {jsonFile}.")
        return None, None, None, None, None, f"Erreur: Impossible de décoder le fichier JSON {jsonFile}."
    except Exception as e:
        logging.error(f"Une erreur s'est produite lors du chargement des chemins à partir du fichier JSON : {str(e)}")
        return None, None, None, None, None, f"Une erreur s'est produite lors du chargement des chemins à partir du fichier JSON : {str(e)}"

def manageTorrentAndJson(pathSourceDirJson, pathSourceDirTorrent, pathInputDirDeluge, queueJson):
    """
    Gère les fichiers torrent et JSON.
    """
    while True:
        try:
            fileJson, error = torrentAndJsonManagement.torrentAndJsonManagementMain(pathSourceDirJson, pathSourceDirTorrent, pathInputDirDeluge)
            if error:
                if error != "No torrent file found.":
                    logging.error(f"Une erreur s'est produite lors de la gestion du torrent et du JSON : {error}")
            elif fileJson is not None:  # Si fileJson est None, aucun fichier torrent n'a été trouvé
                logging.info("Téléchargement en cours ...")
                queueJson.put(fileJson)  # Ajouter le fileJson dans la file d'attente
        except Exception as e:
            logging.error(f"Une erreur s'est produite lors de la gestion du torrent et du JSON : {str(e)}")

def initSortFiles(pathNewDirMedia):
    """
    Crée un fichier appelé 'listFileSought' dans le répertoire spécifié s'il n'existe pas déjà.

    Args:
        pathNewDirMedia (str): Le chemin du répertoire où créer le fichier.

    Returns:
        str: Le chemin complet du fichier créé ou existant.
    """
    file_path = os.path.join(pathNewDirMedia, "listFileSought") # Construire le chemin complet du fichier

    # Vérifier si le fichier existe déjà
    if os.path.exists(file_path):
        logging.info(f"Le fichier 'listFileSought' existe déjà à l'emplacement : {file_path}")
        return file_path  # Retourner le chemin complet du fichier existant

    try:
        # S'il n'existe pas, créer le fichier en mode écriture et le fermer immédiatement pour le créer
        with open(file_path, 'w') as file:
            pass
        
        logging.info(f"Le fichier 'listFileSought' a été créé avec succès à l'emplacement : {file_path}")
        return file_path  # Retourner le chemin complet du fichier créé
    except Exception as e:
        raise Exception(f"Erreur lors de la création du fichier 'listFileSought': {str(e)}")

def sortFiles(pathOutputDirDeluge, pathNewDirMedia, queueJson):
    """
    Trie les fichiers.
    """
    file_listNameFileSought = initSortFiles(pathNewDirMedia)
    while True:
        try:
            try :
                fileJson = queueJson.get_nowait()  # Récupérer le fileJson de la file d'attente
            except :
                fileJson = None
            nameMediaDownloaded = fileSorting.fileSortingMain(pathOutputDirDeluge, pathNewDirMedia, fileJson, file_listNameFileSought)
            if nameMediaDownloaded is not None:
                logging.info(f"Fichier {nameMediaDownloaded} téléchargé et trié avec succès")
        except ValueError as e:
            logging.error(f"Value Error {str(e)}")
        except Exception as e:
            logging.error(f"Une erreur s'est produite lors du tri des fichiers : {str(e)}")

def signalHandler(sig, frame):
    logging.info('Exit ...')
    os._exit(1)

if __name__ == "__main__":
    try:
        configure_logging()  # Configurer le logging

        # Charge les chemins configurés dans le fichier path.json dans le dossier config
        pathSourceDirJson, pathSourceDirTorrent, pathInputDirDeluge, pathOutputDirDeluge, pathNewDirMedia, error = loadPaths(os.path.join('config', 'path.json'))  
        if error:
            logging.error(f"Une erreur s'est produite lors du chargement des chemins dans le fichier path.json dans le dossier config/ : {error}")
        else:
            logging.info("Chargement des chemins réalisé avec succès")

            # Création de la file d'attente partagée
            queueJson = multiprocessing.Queue()

            # Création des processus
            torrentProcess = multiprocessing.Process(target=manageTorrentAndJson, args=(pathSourceDirJson, pathSourceDirTorrent, pathInputDirDeluge, queueJson))
            sortingProcess = multiprocessing.Process(target=sortFiles, args=(pathOutputDirDeluge, pathNewDirMedia, queueJson))

            # Gestion de l'interruption clavier
            signal.signal(signal.SIGINT, signalHandler)

            # Démarrage des processus
            torrentProcess.start()
            sortingProcess.start()

            # Attente que les processus se terminent
            torrentProcess.join()
            sortingProcess.join()
                
    except Exception as e:
        logging.error(f"Une erreur s'est produite dans le main.py: {str(e)}")
