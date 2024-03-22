import os
import signal
import multiprocessing
import websocket
import time

from logger_config import logger
import common
import torrentAndJsonManagement
import fileSorting

def manageTorrentAndJson(pathSourceDirJson, pathSourceDirTorrent, pathInputDirDeluge, queueJson):
    """
    Gère les fichiers torrent et JSON.
    """
    print("Process manageTorrentAndJson() is running ...")
    while True:
        try:
            fileJson, error = torrentAndJsonManagement.torrentAndJsonManagementMain(pathSourceDirJson, pathSourceDirTorrent, pathInputDirDeluge)
            if error:
                if error != "No torrent file found.":
                    logger.error(f"[ERR] : Une erreur s'est produite lors de la gestion du torrent et du JSON : {error}")
            elif fileJson is not None:  # Si fileJson est None, aucun fichier torrent n'a été trouvé
                logger.info(f"[OK] : Téléchargement en cours ... ")
                queueJson.put(fileJson)  # Ajouter le fileJson dans la file d'attente
        except Exception as e:
            print(f"Une erreur s'est produite lors de la gestion du torrent et du JSON : {str(e)}")

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
        logger.info(f"[INFOS] : Le fichier 'listFileSought' existe déjà à l'emplacement : {file_path}")
        return file_path  # Retourner le chemin complet du fichier existant

    try:
        # S'il n'existe pas, créer le fichier en mode écriture et le fermer immédiatement pour le créer
        with open(file_path, 'w') as file:
            pass
        
        logger.info(f"[OK] : Le fichier 'listFileSought' a été créé avec succès à l'emplacement : {file_path}")
        return file_path  # Retourner le chemin complet du fichier créé
    except Exception as e:
        raise Exception(f"Erreur lors de la création du fichier 'listFileSought': {str(e)}")

def sortFiles(pathOutputDirDeluge, pathNewDirMedia, queueJson):
    """
    Trie les fichiers.
    """
    print("Process sortFiles() is running ...")
    file_listNameFileSought = initSortFiles(pathNewDirMedia)
    
    while True:
        try:
            # Tentative de connexion au websocket
            # print("Attempting to connect to websocket client ...")
            ws = websocket.create_connection("ws://localhost:8080")
            # print("Websocket client connected !")
            
            # Boucle principale
            while ws.connected:
                try:
                    # Obtention d'un élément de la file JSON
                    try:
                        fileJson = queueJson.get_nowait()
                    except:
                        fileJson = None
                    
                    # Tri des fichiers
                    nameMediaDownloaded = fileSorting.fileSortingMain(pathOutputDirDeluge, pathNewDirMedia, fileJson, file_listNameFileSought)
                    if nameMediaDownloaded is not None:
                        # Envoi du fichier trié via le websocket
                        ws.send(nameMediaDownloaded)
                        logger.info(f"[OK] : Fichier {nameMediaDownloaded} téléchargé et trié avec succès")
                        
                except ValueError as e:
                    logger.error(f"[ERR] : Value Error {str(e)}")
                except Exception as e:
                    logger.error(f"[ERR] : Sortfiles error : {str(e)}")

        except ConnectionRefusedError as e:
            logger.error(f"[ERR] : Websocket connection refused. Check that the websocket server is running")
            time.sleep(4)
            
        except Exception as e:
            logger.error(f"[ERR] : {str(e)}")
            break

def signalHandler(sig, frame):
    logger.info('[INFOS] : Exit ...')
    os._exit(1)

if __name__ == "__main__":
    try:
        # Charge les chemins configurés dans le fichier path.json dans le dossier config
        (
            pathSourceDirJson,
            pathSourceDirTorrent,
            pathInputDirDeluge,
            pathOutputDirDeluge,
            pathNewDirMedia,
            error,
        ) = common.loadPaths(os.path.join(os.path.dirname(__file__), "../config", "config.json"))
        if error:
            logger.error(f"[ERR] : {error}")
        else:
            logger.info("Chargement des chemins réalisé avec succès")  # Utilisation du logger pour enregistrer les informations

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
        logger.error(f"[ERR]: {str(e)}")
        print(f"Une erreur s'est produite dans le main.py: {str(e)}")

