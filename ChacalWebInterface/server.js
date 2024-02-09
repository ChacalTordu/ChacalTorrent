const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const upload = multer({ dest: 'uploads/' });

// Middleware
app.use(cors());
app.use(express.json()); // Prise en charge des données JSON
app.use(express.urlencoded({ extended: true })); // Prise en charge des données encodées dans l'URL

// Route POST pour le téléchargement de fichiers
app.post('/upload', upload.single('file'), (req, res) => {
  try {
    if (!req.file) {
      throw new Error('Aucun fichier téléchargé.');
    }

    const uploadedFile = req.file;
    const destinationPath = path.join(__dirname, 'tests', 'loadedFiles', uploadedFile.originalname);
    const jsonData = req.body;
    console.log('Données JSON reçues :', jsonData);

    // Déplacer le fichier téléchargé vers le dossier de destination
    fs.renameSync(uploadedFile.path, destinationPath);

    res.send('Fichier téléchargé avec succès !');
  } catch (error) {
    console.error('Une erreur est survenue lors du téléchargement du fichier :', error.message);
    res.status(500).send('Une erreur est survenue lors du téléchargement du fichier.');
  }
});

const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`Serveur HTTP démarré sur le port ${port}`);
});
