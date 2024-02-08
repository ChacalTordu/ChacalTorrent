const express = require('express')
const multer = require('multer')
const fs = require('fs')
const path = require('path')
const cors = require('cors')

const app = express()
const upload = multer({ dest: 'uploads/' })

app.use(cors())
app.use(express.json())

app.post('/upload', upload.single('file'), (req, res) => {
  try {
    // Vérifier si un fichier a été téléchargé
    if (!req.file) {
      throw new Error('Aucun fichier téléchargé.');
    }

    // Récupérer le fichier téléchargé et les données JSON
    const uploadedFile = req.file
    const destinationPath = 'tests/loadedFiles/' + uploadedFile.originalname
    const jsonData = req.body
    console.log(jsonData)

    // Renommer et déplacer le fichier téléchargé
    fs.renameSync(uploadedFile.path, destinationPath)

    // Répondre au client avec succès
    res.send('Fichier téléchargé !');
  } catch (error) {
    // Gérer les erreurs
    console.error('Une erreur est survenue lors du téléchargement du fichier :', error.message)
    res.status(500).send('Une erreur est survenue lors du téléchargement du fichier.')
  }
});


const port = process.env.PORT || 3000

app.listen(port, () => {
  console.log(`Serveur http post démarré sur le port ${port}`)
});
