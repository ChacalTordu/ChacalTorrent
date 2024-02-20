import os
import json
import signal
import multiprocessing

import torrentAndJsonManagement
import fileSorting

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
            print(f"Erreur: Le fichier {jsonFile} n'existe pas.")
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
                print(f"Erreur: Le fichier {jsonFile} est vide.")
                return None, None, None, None, None, f"Erreur: Le fichier {jsonFile} est vide."
    except FileNotFoundError:
        print(f"Erreur: Le fichier {jsonFile} n'existe pas.")
        return None, None, None, None, None, f"Erreur: Le fichier {jsonFile} n'existe pas."
    except json.JSONDecodeError:
        print(f"Erreur: Impossible de décoder le fichier JSON {jsonFile}.")
        return None, None, None, None, None, f"Erreur: Impossible de décoder le fichier JSON {jsonFile}."
    except Exception as e:
        print(f"Une erreur s'est produite lors du chargement des chemins à partir du fichier JSON : {str(e)}")
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
                    print(f"[ERR] : Une erreur s'est produite lors de la gestion du torrent et du JSON : {error}")
            elif fileJson is not None:  # Si fileJson est None, aucun fichier torrent n'a été trouvé
                print(f"[OK] : Torrent déplacé vers {pathInputDirDeluge} avec succès")
                queueJson.put(fileJson)  # Ajouter le fileJson dans la file d'attente
        except Exception as e:
            print(f"Une erreur s'est produite lors de la gestion du torrent et du JSON : {str(e)}")

def sortFiles(pathOutputDirDeluge, pathNewDirMedia, queueJson):
    """
    Trie les fichiers.
    """
    while True:
        try:
            fileJson = queueJson.get()  # Récupérer le fileJson de la file d'attente
            if fileJson is None:
                pass
            else:
                error = fileSorting.fileSortingMain(pathOutputDirDeluge, pathNewDirMedia, fileJson)
                if error is not None:
                    print(f"[ERR] : Une erreur s'est produite lors du tri : {error}")
                else:
                    print("[OK] : Le tri s'est déroulé avec succès")
        except Exception as e:
            print(f"Une erreur s'est produite lors du tri des fichiers : {str(e)}")

def signalHandler(sig, frame):
    print('[INFOS] : Exit ...')
    os._exit(1)

if __name__ == "__main__":
    try:
        # Charge les chemins configurés dans le fichier path.json dans le dossier config
        pathSourceDirJson, pathSourceDirTorrent, pathInputDirDeluge, pathOutputDirDeluge, pathNewDirMedia, error = loadPaths(os.path.join('config', 'path.json'))  
        if error:
            print(f"[ERR] : Une erreur s'est produite lors du chargement des chemins dans le fichier path.json dans le dossier config/ : {error}")
        else:
            print("[OK] : Chargement des chemins réalisé avec succès")

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
        print(f"Une erreur s'est produite dans le main.py: {str(e)}")
