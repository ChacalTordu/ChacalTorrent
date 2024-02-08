const express = require('express');
const multer = require('multer');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const upload = multer({ dest: 'uploads/' });

app.use(cors());

app.post('/upload', upload.single('file'), (req, res) => {
  const uploadedFile = req.file;
  const destinationPath = 'tests/loadedFiles/' + uploadedFile.originalname;
  fs.renameSync(uploadedFile.path, destinationPath);
  res.send('Fichier téléchargé !');
});

const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`Serveur http post démarré sur le port ${port}`);
});
