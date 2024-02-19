import os
import shutil

def checkDuplicateFiles(sourceDirJson, sourceDirTorrent, inputDirDeluge):
    """
    Vérifie la duplication des fichiers .json et .torrent dans deux dossiers différents.

    Args:
        sourceDirJson (str): Chemin vers le répertoire contenant les fichiers .json.
        sourceDirTorrent (str): Chemin vers le répertoire contenant les fichiers .torrent.
        inputDirDeluge (str): Chemin vers le répertoire de destination pour les fichiers .torrent.

    Returns:
        tuple: Un tuple contenant le nom du fichier torrent et le fichier JSON correspondant, ou (None, None) s'il n'y a pas de duplication.
    """
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

def moveTorrentToDeluge(path_sourceDirTorrent, path_inputDirDeluge, fileTorrent):
    """
    Move a .torrent file to a specified directory.

    Args:
        path_inputDirDeluge (str): Path to the destination directory for the .torrent file.
        fileTorrent (str): Name of the .torrent file to be moved.

    Returns:
        str or None: Error message if an error occurs, None otherwise.
    """
    try:
        sourcePath = os.path.join(path_sourceDirTorrent, fileTorrent)
        targetPath = os.path.join(path_inputDirDeluge, fileTorrent)
        shutil.move(sourcePath, targetPath)
        return None  # No error occurred, return None
    except FileNotFoundError as e:
        return f"Error: {e.strerror} ({e.filename})"

def torrentAndJsonManagementMain(path_sourceDirJson, path_sourceDirTorrent, path_inputDirDeluge):
    """
    Main function for managing torrents and JSON files.

    Args:
        path_sourceDirJson (str): Path to the directory containing .json files.
        path_sourceDirTorrent (str): Path to the directory containing .torrent files.
        path_inputDirDeluge (str): Path to the destination directory for .torrent files.

    Returns:
        tuple: A tuple containing the name of the torrent file and the name of the created media,
        or (None, None, error_torrentAndJsonManagementMain) in case of error.
    """
    try:
        file_torrent, file_json = checkDuplicateFiles(path_sourceDirJson, path_sourceDirTorrent, path_inputDirDeluge)
        if file_torrent:
            if not moveTorrentToDeluge(path_sourceDirTorrent, path_inputDirDeluge, file_torrent):
                if file_json:
                    return file_json, None
        else:
            return None, f"No torrent file found."
    except Exception as error:
        return None, error
