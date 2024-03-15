const express = require('express');
const websocketRoutes = require('./routes/websocketRoutes');

const app = express();

// Montage des routes WebSocket sur l'application express principale
app.use('/websocket', websocketRoutes);

module.exports = app;
