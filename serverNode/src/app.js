const express = require('express');
const http = require('http');
const websocketRoute = require('./modules/websocket/index');
const app = express();

// Créer un serveur HTTP avec Express
const server = http.createServer(app);

// Lancer le serveur HTTP
const PORT = process.env.PORT || 3000;

server.listen(PORT, () => {
  console.log(`Serveur HTTP démarré sur le port ${PORT}`);
});

// Monter les routes WebSocket sur l'application express principale
app.use('/websocketStart', websocketRoute);
