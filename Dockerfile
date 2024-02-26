# Utiliser une image de base avec Node.js et Python
FROM node:18

# Installer Python et ses dépendances
RUN apt-get update && apt-get install -y python3 python3-pip

# Répertoire de travail dans le conteneur
WORKDIR /ChacalTorrent

# Copier les fichiers locaux dans le conteneur
COPY . .

# Installer les dépendances Node.js si un package-lock.json ou un fichier package.json est présent
RUN [ -f package-lock.json ] && npm ci || npm install

# Installer les dépendances Python
COPY ChacalFileManagement/requirements.txt .
RUN pip install -r requirements.txt

# Exposer le port utilisé par votre application Vue.js
EXPOSE 1998

# Commande pour construire et démarrer l'application Vue.js, le script Python et le serveur back
CMD npm run build && npm install -g http-server && http-server -p 1998 -c-1 ./dist & python3 ChacalFileManagement/main.py & node ChacalWebManagement/serverBack/server.js
