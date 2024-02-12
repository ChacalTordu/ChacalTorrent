const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const cors = require('cors');
const { ref } = require('vue');

// Définir les dossiers de destination
const uploadDestination = 'uploadsTorrent/';
const jsonDestination = 'uploadsJSON/';
let fileName = ''; // Utiliser let au lieu de const car la valeur sera modifiée

const app = express();
const upload = multer({ dest: uploadDestination });

// Definir le port d'écoute
const port = process.env.PORT || 3000;

// Configuration du CORS
app.use(cors());

// Middleware
app.use(express.json()); // Prise en charge des données JSON
app.use(express.urlencoded({ extended: true })); // Prise en charge des données encodées dans l'URL

// Route POST pour le téléchargement de fichiers
app.post('/uploadFile', upload.single('file'), (req, res) => {
  try {
    if (!req.file) {
      throw new Error('Aucun fichier téléchargé.');
    }

    const uploadedFile = req.file;
    const destinationPath = path.join(__dirname, uploadDestination, uploadedFile.originalname);

    // Déplacer le fichier téléchargé vers le dossier de destination
    fs.renameSync(uploadedFile.path, destinationPath);

    // Récupérer le nom du fichier téléchargé sans l'extension
    fileName = path.parse(uploadedFile.originalname).name;

    res.send('Fichier téléchargé avec succès !');

  } catch (error) {
    console.error('Une erreur est survenue lors du téléchargement du fichier :', error.message);
    res.status(500).send('Une erreur est survenue lors du téléchargement du fichier.');
  }
});

// Route POST pour les données JSON
app.post('/uploadJSON', (req, res) => {
  try {
    const jsonData = req.body;
    writeJSONToFile(jsonData);
    res.send('Données JSON reçues avec succès !');
  } catch (error) {
    console.error('Une erreur est survenue lors de la réception des données JSON :', error.message);
    res.status(500).send('Une erreur est survenue lors de la réception des données JSON.');
  }
});

// Fonction d'écriture du fichier JSON
function writeJSONToFile(jsonData) {
  try {
    // Chemin du fichier JSON à écrire
    const filePath = path.join(__dirname, jsonDestination, fileName + '.json');

    // Convertir les données JSON en chaîne JSON
    const jsonString = JSON.stringify(jsonData, null, 2);

    // Écrire les données JSON dans le fichier
    fs.writeFileSync(filePath, jsonString);

    // console.log('Données JSON écrites avec succès dans le fichier:', filePath);
  } catch (error) {
    console.error('Une erreur est survenue lors de l\'écriture des données JSON dans le fichier :', error.message);
  }
}

app.listen(port, () => {
  console.log(`Serveur HTTP démarré sur le port ${port}`);
});
