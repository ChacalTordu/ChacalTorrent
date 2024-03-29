# ChacalTorrentInterface

Ce projet est une interface simplifiée pour le téléchargement de fichiers .torrent sur un serveur. Il est conçu pour faciliter le processus de téléchargement de fichiers .torrent et d'organisation des données associées. Veuillez noter que ce projet n'encourage en aucun cas les téléchargements illégaux. Il est à but éducatif et de découverte. L'utilisateur est responsable de l'utilisation légale de ce projet.

Ce projet est découpé en plusieurs parties :

- **Interface Web Vue.js** : Une interface utilisateur construite avec Vue.js pour rentrer le fichier .torrent à télécharger ainsi que les informations nécéssaire du média concerné.

- **Outil d'organisation en Python** : Une partie du projet écrite en Python pour l'organisation des fichiers après leur téléchargement. Cette partie peut être personnalisée en fonction des besoins de l'utilisateur.

Veuillez noter que l'utilisateur est responsable de la mise en place d'un système de téléchargement. Ce projet ne prend pas en charge cette fonctionnalité.

## Architecture logiciel

![Architecture logiciel Chacal Torrent](Archi_ChacalTorrent.svg)

## Guide d'installation et de lancement du projet ChacalTorrent

Ce guide vous aidera à démarrer le projet ChacalTorrent sur une machine vierge. Assurez-vous d'avoir les privilèges d'administrateur et une connexion Internet active pour effectuer toutes les étapes.

### Prérequis

Avant de commencer, assurez-vous que votre système dispose des éléments suivants installés :

- [Docker](https://www.docker.com/get-started) : Utilisé pour la gestion des conteneurs et le déploiement de l'application.
- [Git](https://git-scm.com/) : Pour cloner le dépôt du projet.

### Instructions

1. **Cloner le dépôt du projet** :

    Ouvrez un terminal et exécutez la commande suivante :
    ```
    git clone https://github.com/ChacalTordu/ChacalTorrent.git
    ```

2. **Accéder au répertoire du projet** :

    ```
    cd ChacalTorrent
    ```
3. **Éditer le fichier de configuration `config/config.json`** :

Pour configurer les dossiers selon vos besoins, suivez les étapes ci-dessous :

1. Créez le dossier de configuration et le fichier `config.json` en utilisant les commandes suivantes :
   
    ```bash
    mkdir -p config && touch config/config.json
    ```

2. Utilisez un éditeur de texte pour ouvrir le fichier `config/config.json`. Par exemple, vous pouvez utiliser Vim :

    ```bash
    vim ./config/config.json
    ```

3. Dans l'éditeur de texte, copiez, collez et modifier les chemins et la clé TMDB, dans le fichier `config.json`, selon vos besoins :

    ```json
    {
        "path_sourceDirJson": "../",
        "path_sourceDirTorrent": "../",
        "path_inputDirDeluge": "../",
        "path_outputDirDeluge": "../",
        "path_mediaDir": "../",
        "path_mediaDirMovie": "~/",
        "path_mediaDirCartoon": "~/",
        "path_mediaDirShows": "~/",
        "path_mediaDirAnime": "~/",
        "apiKey_tmdb": "abcdefghijklmnopqrstuvwxyz"
    }
    ```
    **Attention !!!** Lors de la spécification des chemins pour `path_mediaDirMovie`, `path_mediaDirCartoon`, `path_mediaDirShows` et `path_mediaDirAnime`, veuillez utiliser le chemin complet de destination. Pour les autres chemins, assurez-vous qu'ils sont relatifs par rapport au fichier `config.json`. Avant d'exécuter le programme, assurez-vous d'avoir les droits d'écriture nécessaires sur tous les chemins indiqués.

4. Modifiez les chemins des dossiers selon vos besoins.

5. Une fois que vous avez terminé d'éditer le fichier, appuyez sur `Esc` pour quitter le mode édition, puis tapez `:wq` pour enregistrer les modifications et quitter Vim.

Une fois que vous avez configuré les chemins des dossiers et enregistré les modifications dans `config.json`, votre application devrait être prête à être utilisée.

4. **Construire l'image Docker** :

    ```
    docker build -t chacaltorrent .
    ```

5. **Démarrer le conteneur Docker** :
    Pour démarrer le conteneur Docker et exposer les ports 1998, 3000 et 8080 sur votre machine hôte, utilisez la commande suivante. Nous limitons également l'utilisation du CPU à 10% pour éviter tout risque de crash, et de surconsommation. Cela est dû au multiprocessing de Python.

    ```
    docker run -d --restart unless-stopped \
    --cpus=0.1 \
    -p 1998:1998 -p 3000:3000 -p 8080:8080 \
    chacaltorrent
    ```

6. **Accéder à l'application** :

    Ouvrez un navigateur web et accédez à l'URL suivante :
    ```
    http://{IP.de.votre.serveur}:1998/
    ```
