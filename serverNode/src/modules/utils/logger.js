// logger.js

// Fonction pour obtenir la date et l'heure actuelles au format ISO
function getCurrentTimestamp() {
    return new Date().toISOString();
  }
  
  // Fonction de journalisation de message d'information
  function info(message) {
    console.log(`[${getCurrentTimestamp()}] INFO: ${message}`);
  }
  
  // Fonction de journalisation de message d'erreur
  function error(message) {
    console.error(`[${getCurrentTimestamp()}] ERROR: ${message}`);
  }
  
  // Exportation des fonctions de journalisation
  module.exports = { info, error };
  