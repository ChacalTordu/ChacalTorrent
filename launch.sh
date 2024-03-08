echo "Starting Backend server..."
node ./ChacalWebInterface/serverBack/server.js
echo "Running FileManager..."
python3 ChacalFileManagement/main.py &
echo "Launching Front interface..."
npm run preview --prefix ChacalWebInterface -- --host --port 1998 &