const express = require('express');
const router = express.Router();
const { startWebSocketServer } = require('../controllers/websocketController');

router.get('/websocketStart', function (req, res) {
  startWebSocketServer();
  res.send('WebSocket server ON');
});

module.exports = router;
