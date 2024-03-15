const fs = require('fs');
const path = require('path');

// Function to ensure directory exists, create if not
function ensureDirectoryExists (directory) {
  if (!fs.existsSync(directory)) {
    fs.mkdirSync(directory, { recursive: true });
  }
};

/**
 * Writes JSON Data to File
 * Writes received JSON data to a file in JSON format.
 * @param {Object} jsonData - JSON data to be written to file
 */
function writeJSONToFile(jsonData) {
  try {
    // File path to write JSON
    const filePath = path.join(__dirname, jsonDestination, fileName + '.json');

    // Convert JSON data to JSON string
    const jsonString = JSON.stringify(jsonData, null, 2);

    // Write JSON data to file
    fs.writeFileSync(filePath, jsonString);

    // console.log('Données JSON écrites avec succès dans le fichier:', filePath);
  } catch (error) {
    console.error('Une erreur est survenue lors de l\'écriture des données JSON dans le fichier :', error.message); // Error writing JSON data to file
  }
}

// Ensure directories exist
ensureDirectoryExists(path.join(__dirname, uploadDestination));
ensureDirectoryExists(path.join(__dirname, jsonDestination));

