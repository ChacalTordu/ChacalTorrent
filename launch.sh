echo "Running FileManager..."
python3 ChacalFileManagement/main.py &
echo "Launching Front interface..."
npm install --prefix ChacalWebInterface &&
npm run preview --prefix ChacalWebInterface -- --host --port 1998 &
echo "Installing Backend dependencies..."
npm install --prefix serverNode &&
echo "Starting Backend server..."
node ./serverNode/src/index.js
