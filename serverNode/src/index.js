const express = require('express');
const cors = require('cors');
const httpHandler = require('./modules/httpHandler');
const websocketServer = require('./modules/websocketServer');

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

httpHandler.startHTTPServer(app);

websocketServer.startWebSocketServer();

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Http post listening on ${PORT} ...`);
});
