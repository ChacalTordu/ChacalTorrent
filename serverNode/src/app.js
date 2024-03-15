const express = require('express');
const http = require('http');
const websocketRoute = require('./modules/websocketRoute');
const app = express();

// Créer un serveur HTTP avec Express
const server = http.createServer(app);

// Monter le routeur WebSocket sur votre application Express
app.use('/websocket', websocketRoute);

// Lancer le serveur HTTP
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Serveur HTTP démarré sur le port ${PORT}`);
});
