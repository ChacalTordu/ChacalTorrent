echo "Running FileManager..."
python3 ChacalFileManagement/main.py &

echo "Launching Front interface..."
serve -s ChacalWebInterface/dist -l 1998 &

echo "Running Backend server..."
node ./serverNode/src/index.js
