# Utiliser une image de base avec Node.js et Python
FROM node:18

# Installer Python et ses dépendances
RUN apt-get update && apt-get install -y python3 python3-pip

# Créer le répertoire de travail dans le conteneur
WORKDIR /ChacalTorrent

# Copier les fichiers locaux dans le conteneur
COPY . .

# Installer les dépendances Node.js si un package-lock.json ou un fichier package.json est présent
WORKDIR /ChacalTorrent/ChacalWebInterface
RUN npm install && npm run build

# Installer les dépendances Python
WORKDIR /ChacalTorrent/ChacalFileManagement
RUN pip install -r requirements.txt --break-system-packages

# Installer les dépendances Node.js si un package-lock.json ou un fichier package.json est présent dans le serverNode
WORKDIR /ChacalTorrent/serverNode
RUN npm install --prefix serverNode

# Exposer les ports
EXPOSE 3000
EXPOSE 1998
EXPOSE 8080

# Définir le répertoire de travail par défaut
WORKDIR /ChacalTorrent

# Commande pour démarrer les différentes parties de l'application
CMD ["./launch.sh"]
