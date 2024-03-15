const fs = require('fs');
const path = require('path');

const uploadFile = (req, res) => {
  try {
    if (!req.file) {
      throw new Error('Aucun fichier téléchargé.'); // No file uploaded
    }

    const uploadedFile = req.file;
    const jsonData = req.body;

    const destinationPath = path.join(__dirname, '..', uploadDestination, uploadedFile.originalname);
    const filePath = path.join(__dirname, '..', jsonDestination, uploadedFile.originalname + '.json');

    // Déplacer le fichier téléchargé vers le dossier de destination
    fs.renameSync(uploadedFile.path, destinationPath);

    // Convertir les données JSON en chaîne JSON
    const jsonString = JSON.stringify(jsonData, null, 2);

    // Écrire les données JSON dans le fichier
    fs.writeFileSync(filePath, jsonString);

    res.send('Fichier téléchargé et données JSON reçues avec succès !'); // File uploaded and JSON data received successfully

  } catch (error) {
    console.error('Une erreur est survenue lors du téléchargement du fichier ou de la réception des données JSON :', error.message); // Error during file upload or receiving JSON data
    res.status(500).send('Une erreur est survenue lors du téléchargement du fichier ou de la réception des données JSON.'); // Error response
  }
};

module.exports = { uploadFile };
