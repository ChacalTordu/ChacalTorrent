import express, { json, urlencoded } from 'express';
import cors from 'cors';
import { startHTTPServer } from './modules/httpHandler';
import { startWebSocketServer } from './modules/websocketServer';

const app = express();

app.use(cors());
app.use(json());
app.use(urlencoded({ extended: true }));

startHTTPServer(app);

startWebSocketServer();

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`http post listening on ${PORT} ...`);
});
