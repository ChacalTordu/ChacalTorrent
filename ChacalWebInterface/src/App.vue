<template>
  <div class="myApp">
    <div class="twoZone">
      <ZoneDropFile :class="{ 'blink': isBlinking && !torrentValid }" @fileChosen="saveTorrent" @resetButton="resetButtonValue" @abordClicked="handleAbortZoneDropClicked"/>
      <ZoneFileInfo :class="{ 'blink': isBlinking && !dataValid }" @saveMediaData="saveMediaInfo"  @resetButton="resetButtonValue" @abortClicked="handleAbortFileInfoClicked"/>
    </div>
    <div class="buttonAndSpinner">
      <ButtonConfirm :class="{ 'visible': !downloadingFlag, 'noneVisible': downloadingFlag || downloadSuceed || downloadError}" textButton="Télécharger" @confirmClicked="handleConfirmClicked" />
      <Spinner v-if="downloadingFlag"/>
      <Sucess :class="{ 'visible': downloadSuceed, 'noneVisible': !downloadSuceed }"/>
      <Error :class="{ 'visible': downloadError, 'noneVisible': !downloadError }"/>
    </div>
    <ZoneLogInfos :logMessages="logMessages" />
  </div>
</template>


<script setup>
  import ZoneDropFile from "./components/ZoneDropFile.vue"
  import ZoneFileInfo from "./components/ZoneFileInfos.vue"
  import ButtonConfirm from "./components/button/ButtonConfirm.vue"
  import Spinner from "./components/animation/Spinner.vue"
  import Sucess from "./components/animation/Sucess.vue"
  import Error from "./components/animation/Error.vue"
  import ZoneLogInfos from "./components/ZoneLogInfos.vue"

  import axios from 'axios'
  import { ref } from 'vue'

  const downloadingFlag = ref(false)
  const downloadSuceed = ref(false)
  const downloadError = ref(false)

  const isBlinking = ref(false)

  const dataValid = ref(false);
  const torrentValid = ref(false)

  const fileTorrent = ref(null)
  const formData = new FormData();
  var jsonMediaInfos
  
  const confirmClick = ref(false)

  const mediaType = ref('')
  const mediaMultipleSeason = ref(false)
  const mediaAlreadyExist = ref(false)
  const pathMedia = ref('')

  const ws = new WebSocket('ws://localhost:8080');
  const logMessages = ref([]);

  // Envoi le JSON et le fichier torrent au serveur
  async function sendDataToServer() {
    try {
      // Vérification du flag pour le fichier .torrent
      if (torrentValid.value) {
        await axios.post('http://localhost:3000/uploadFile', formData);
        console.log('Fichier téléchargé avec succès sur le serveur !');
      }
      // Vérification du flag pour les données JSON
      if (dataValid.value) {
        await axios.post('http://localhost:3000/uploadJSON', jsonMediaInfos);
        console.log('Json téléchargé avec succès sur le serveur !');
      }
      return true  
    } catch (error) {
      console.error('Une erreur est survenue lors de l\'envoi des données au serveur:', error.message);
      return false
    }
  }

  function saveTorrent(file) {
    try {
      fileTorrent.value = file;
      formData.set('file', fileTorrent.value);
      // Flag à vrai
      torrentValid.value = true;
      // console.log("Torrent sauvegardé correctement")
    } catch(error) {
      console.error('Erreur lors de la sauvegarde des données du fichier .torrent:', error.message);
    }
  }

  function saveMediaInfo(saveMediaType, savePathMedia, saveCheckbox1, saveCheckbox2) {
    try {
      mediaType.value = saveMediaType.value;
      mediaMultipleSeason.value = saveCheckbox1;
      mediaAlreadyExist.value = saveCheckbox2;
      pathMedia.value = savePathMedia.value;
      if (formattingJsonFile()) {
        dataValid.value = true;
      }
    } catch (error) {
      console.error('Erreur lors de la sauvegarde des données du média (json):', error.message);
    }
  }

  function formattingJsonFile() {
    try{
      var mediaInfos = {
          "mediaType": mediaType.value,
          "boolMediaMultipleSeason": mediaMultipleSeason.value,
          "boolAlreadyExist": mediaAlreadyExist.value,
          "NameMedia": pathMedia.value,
        };
        jsonMediaInfos = JSON.stringify(mediaInfos);
        // console.log("JSON formaté :", jsonMediaInfos);
        return true
    }catch(error){
      console.error('Erreur lors de l attribution des données du média (json):', error.message);
      return false
    }
  }

  function handleConfirmClicked() {
    try {
      confirmClick.value = true;
      if (dataValid.value && torrentValid.value) {
        downloadingFlag.value = true // On passe dans un état de téléchargement
        formattingJsonFile()
        if(sendDataToServer()){
          downloadSuceed.value = true
        }else{
          downloadError.value = true
        }
        downloadingFlag.value = false // Fin du téléchargement
      }else{
        if (!dataValid.value) {
          blinkdiv();
        } else if (!torrentValid.value) {
          blinkdiv();
        }
        console.log("Un des deux flags est à faux :\njson flag value :",dataValid.value,"\ntorrent flag value :",torrentValid.value)
      }
    } catch (error) {
      console.error('Une erreur est survenue lors du traitement du clic sur le bouton :', error.message);
    }
  }

  function handleAbortZoneDropClicked(){
    resetTorrentFlag()
    // resetJsonDataValid()
  }

  function handleAbortFileInfoClicked(){
    resetDataFlag()
  }

  function resetButtonValue() {
    confirmClick.value = false;
  }

  function resetJsonDataValid(){
    // Changer le pathMedia du json par le nouveau nom
    dataValid.value = false
    // alert("Veuillez abort les infos, et re-confirmez (dû à un changement de fichier torrent)")
  }

  function resetTorrentFlag(){
    torrentValid.value = false
  }
  function resetDataFlag(){
    dataValid.value = false
  }

  function blinkdiv() {
    isBlinking.value = true;
    const durations = [200, 400, 600, 800, 1000];
    for (let i = 0; i < durations.length; i++) {
      setTimeout(() => {
        isBlinking.value = !isBlinking.value;
      }, durations[i]);
    }
  }

  ws.onmessage = (event) => {
  logMessages.value = [event.data]; // Remplacer le contenu actuel par le nouveau message
};

</script>

<style scoped>
.myApp {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 60px;
}
.twoZone {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 30px;
}

.blink {
    outline: 2px solid var(--red-color-4); 
  }
  .buttonAndSpinner{
    display: flex;
    flex-direction: row;

    align-items: center;
  }
  .noneVisible{
    display: none;
  }
</style>
