echo "Running FileManager..."
python3 ChacalFileManagement/main.py &
echo "Launching Front interface..."
npm run preview --prefix ChacalWebInterface -- --host --port 1998 &
echo "Starting Backend server..."
node ./serverNode/src/index.js