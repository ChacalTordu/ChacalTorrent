import torrentAndJsonManagement
import fileSorting
import os

if __name__ == "__main__":
    try:
        # Appeler la fonction de gestion du torrent et du JSON
        #       -> Check la duplication de fichier .json et .torrent
        #       -> Move le fichier .torrent dans le dossier inputDeluge
        #       -> Move le fichier/dossier télécharger et le met dans un dossier crée
        nameTorrentWithExtension, nameMedia = torrentAndJsonManagement.torrentAndJsonManagementMain()
        
        nameTorrent, _ = os.path.splitext(nameTorrentWithExtension)  # Séparer le nom du fichier de son extension

        if nameTorrent:  # Vérifier si les noms sont valides
            # Charger les chemins à partir du fichier JSON
            configDir = 'config'
            configJson = os.path.join(configDir, 'path.json')
            paths = torrentAndJsonManagement.loadPathsFromJson(configJson)

            if paths is not None:
                # Récupérer le chemin du répertoire de sortie du déluge
                outputDirDeluge = paths.get('outputDirDeluge')
                if outputDirDeluge:
                    # print("Elements envoyé nameMedia: ",nameMedia)
                    # Appeler la fonction de tri des fichiers/dossiers
                    fileSorting.fileSortingMain(outputDirDeluge, nameTorrent, nameMedia)
                else:
                    print("Erreur: Le chemin du répertoire de sortie du déluge n'est pas spécifié dans le fichier JSON.")
            else:
                print("Erreur: Impossible de charger les chemins à partir du fichier JSON.")
        else:
            print("Erreur: Impossible de gérer le torrent et le JSON.")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
