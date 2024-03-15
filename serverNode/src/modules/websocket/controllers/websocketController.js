const WebSocket = require('ws');

// Fonction de création et gestion du serveur WebSocket
const startWebSocketServer = () => {
  const wss = new WebSocket.Server({ port: 8080 });
  console.log(`WebSocket server listening on port ${port}`);
  
  // Gestion des connexions WebSocket
  wss.on('connection', (ws) => {
    console.log('Client connected to WebSocket server');
    
    // Écoute des messages envoyés par le client
    ws.on('message', (message) => {
      console.log("Message received : ", message)
      wss.clients.forEach(client => {
        if (client.readyState === WebSocket.OPEN) {
          client.send(message);
        }
      });
    });
  });
};

module.exports = { startWebSocketServer };
