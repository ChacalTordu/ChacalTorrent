import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

processed_files = set()

def afficher_contenu():
    print("Choisissez le type de contenu:")
    print("1. Film")
    print("2. Série")
    print("3. AnimeJap")
    print("4. Dessin Animé")

def demander_info():
    afficher_contenu()
    try:
        choix = int(input("Entrez le numéro correspondant au type de contenu: "))
        if choix not in [1, 2, 3, 4]:
            raise ValueError("Choix invalide.")
    except ValueError as e:
        print(f"Erreur: {e}")
        return demander_info()

    type_contenu = {
        1: 'film',
        2: 'série',
        3: 'animejap',
        4: 'dessin animé'
    }[choix]

    titre = input("Entrez le titre: ")

    if type_contenu in ['série', 'animejap']:
        saison = int(input("Entrez le numéro de saison (s'il y en a plusieurs, sinon 1): "))
        sous_dossier = f"Saison {saison}" if saison > 1 else ""
    else:
        sous_dossier = ""

    return type_contenu, titre, sous_dossier

def organiser_fichiers(source_folder, destination_folder, type_contenu, titre, sous_dossier=""):
    # Crée la structure d'arborescence souhaitée
    if type_contenu == 'film':
        destination_path = os.path.join(destination_folder, "Films", titre)
    else:
        destination_path = os.path.join(destination_folder, type_contenu.capitalize(), titre, sous_dossier)

    os.makedirs(destination_path, exist_ok=True)

    # Déplace les fichiers vers le dossier de destination
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f)) and f not in processed_files]
    for file in files:
        processed_files.add(file)
        source_path = os.path.join(source_folder, file)
        shutil.move(source_path, destination_path)
        print(f'{file} déplacé vers {destination_path}')

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        print(f'Nouveau fichier créé: {event.src_path}')
        type_contenu, titre, sous_dossier = demander_info()
        organiser_fichiers(source_folder, destination_folder, type_contenu, titre, sous_dossier)

if __name__ == "__main__":
    source_folder = ''
    destination_folder = ''

    # Surveillance du dossier pour détecter de nouveaux fichiers
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=source_folder, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
