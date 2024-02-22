# ChacalTorrentInterface

Ce projet est une interface simplifiée pour le téléchargement de fichiers .torrent sur un serveur. Il est conçu pour faciliter le processus de téléchargement de fichiers .torrent et d'organisation des données associées. Veuillez noter que ce projet n'encourage en aucun cas les téléchargements illégaux. Il est à but éducatif et de découverte. L'utilisateur est responsable de l'utilisation légale de ce projet.

Ce projet est découpé en plusieurs parties :

- **Interface Web Vue.js** : Une interface utilisateur construite avec Vue.js pour rentrer le fichier .torrent à télécharger ainsi que les informations nécéssaire du média concerné.

- **Outil d'organisation en Python** : Une partie du projet écrite en Python pour l'organisation des fichiers après leur téléchargement. Cette partie peut être personnalisée en fonction des besoins de l'utilisateur.

Veuillez noter que l'utilisateur est responsable de la mise en place d'un système de téléchargement. Ce projet ne prend pas en charge cette fonctionnalité.

## Architecture logiciel

![Architecture logiciel Chacal Torrent](Archi_ChacalTorrent.svg)

## Lancement du projet de test

### Compilation et rechargement à chaud pour le développement
Windows :
```sh
cd .\ChacalWebInterface\
node .\serverBack\server.js
npm run dev
cd ..\ChacalFileManagement\
python.exe .\main.py
```
Linux :
```sh
cd ChacalWebInterface/
node ./serverBack/server.js
npm run dev
cd ../ChacalFileManagement/
python main.py
```
Vous pouvez désormais vous rendre à l'adresse http://localhost:5173/
### Compilation et minification pour la production
```sh
npm run build
```
