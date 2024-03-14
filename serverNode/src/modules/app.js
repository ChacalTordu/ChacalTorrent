const express = require('express');
const logger = require('./utils/logger'); // Importe le module de journalisation personnalisé
const authRoutes = require('./modules/auth/authRoutes'); // Importe les routes d'authentification

const app = express();

// Middleware pour enregistrer les requêtes entrantes
app.use((req, res, next) => {
  logger.info(`${req.method} ${req.url}`);
  next();
});

// Middleware pour parser les requêtes JSON
app.use(express.json());

// Routes d'authentification
app.use('/auth', authRoutes);

// Middleware pour gérer les erreurs
app.use((err, req, res, next) => {
  logger.error(`Error: ${err.message}`);
  res.status(500).json({ error: 'Internal server error' });
});

module.exports = app;
