const fs = require('fs');
const path = require('path');
const multer = require('multer');
const config = require('../../../config/config.json');
let fileName = '';

function startHTTPServer(app) {
  const upload = multer({ dest: path.resolve(__dirname, '..', '..', config.path_sourceDirTorrent) });

  app.post('/uploadFile', upload.single('file'), (req, res) => {
    try {
      if (!req.file) {
        throw new Error('Aucun fichier téléchargé.');
      }

      const uploadedFile = req.file;
      const destinationPath = path.resolve(__dirname, '..', '..', config.path_sourceDirTorrent, uploadedFile.originalname);
      
      fs.renameSync(uploadedFile.path, destinationPath);

      fileName = path.parse(uploadedFile.originalname).name;

      res.send('Fichier téléchargé avec succès !');
    } catch (error) {
      console.error('[ERR] :', error.message);
      res.status(500).send('Une erreur est survenue lors du téléchargement du fichier.');
    }
  });

  app.post('/uploadJSON', (req, res) => {
    try {
      const jsonData = req.body;
      const filePath = path.join(__dirname, '..', '..', config.path_sourceDirJson, fileName + '.json');
      const jsonString = JSON.stringify(jsonData, null, 2);
      fs.writeFileSync(filePath, jsonString);
      res.send('Données JSON reçues avec succès !');
    } catch (error) {
      console.error('[ERR] :', error.message);
      res.status(500).send('Une erreur est survenue lors de la réception des données JSON.');
    }
  });

  ensureDirectoryExists(path.resolve(__dirname, '..', '..', config.path_sourceDirTorrent));
  ensureDirectoryExists(path.resolve(__dirname, '..', '..', config.path_sourceDirJson));
}

function ensureDirectoryExists(directory) {
  if (!fs.existsSync(directory)) {
    fs.mkdirSync(directory, { recursive: true });
  }
}

module.exports = { startHTTPServer };
