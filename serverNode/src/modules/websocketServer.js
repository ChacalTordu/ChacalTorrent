const WebSocket = require('ws');

function startWebSocketServer() {
  const wss = new WebSocket.Server({ port: 8080 });
  console.log(`WebSocket server listening on ${wss.address().port} ...`);

  wss.on('connection', (ws) => {
    console.log('Client connected on WebSocket server');

    ws.on('message', (message) => {
      console.log("Message received : ", message)
      wss.clients.forEach(client => {
        if (client.readyState === WebSocket.OPEN) {
          client.send(message);
        }
      });
    });
  });
}

module.exports = { startWebSocketServer };
