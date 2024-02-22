<!--
App.vue - Main Application Component

This component represents the main application layout and functionality.

Author: ChacalTordu
-->

<template>
  <div class="myApp">
    <div class="twoZone">
      <!-- Zone for dropping files -->
      <ZoneDropFile :class="{ 'blink': isBlinking && !torrentValid }" @fileChosen="saveTorrent" @resetButton="resetButtonValue" @abordClicked="handleAbortZoneDropClicked"/>
      <!-- Zone for displaying file information -->
      <ZoneFileInfo :class="{ 'blink': isBlinking && !dataValid }" @saveMediaData="saveMediaInfo"  @resetButton="resetButtonValue" @abortClicked="handleAbortFileInfoClicked"/>
    </div>
    <div class="buttonAndSpinner">
      <!-- Button for starting download -->
      <ButtonConfirm :class="{ 'visible': !downloadingFlag, 'noneVisible': downloadingFlag || downloadSuceed || downloadError}" textButton="Télécharger" @confirmClicked="handleConfirmClicked" />
      <!-- Spinner indicating download in progress -->
      <Spinner v-if="downloadingFlag"/>
      <!-- Success animation for successful download -->
      <Sucess :class="{ 'visible': downloadSuceed, 'noneVisible': !downloadSuceed }" />
      <!-- Error animation for download failure -->
      <Error :class="{ 'visible': downloadError, 'noneVisible': !downloadError }"/>
    </div>
    <!-- Component for displaying log information -->
    <ZoneLogInfos :logMessages="logMessages" />
    <!-- Information for refreshing page -->
    <p>Si vous souhaitez télécharger un nouveau fichier, veuillez actualiser la page.</p>
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

// Send JSON and torrent file to server
async function sendDataToServer() {
  try {
    if (torrentValid.value) {
      await axios.post('http://localhost:3000/uploadFile', formData);
      console.log('Fichier téléchargé avec succès sur le serveur !');
    }
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

// Save torrent file
function saveTorrent(file) {
  try {
    fileTorrent.value = file;
    formData.set('file', fileTorrent.value);
    torrentValid.value = true;
  } catch(error) {
    console.error('Erreur lors de la sauvegarde des données du fichier .torrent:', error.message);
  }
}

// Save media information
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

// Format JSON file
function formattingJsonFile() {
  try{
    var mediaInfos = {
        "mediaType": mediaType.value,
        "boolMediaMultipleSeason": mediaMultipleSeason.value,
        "boolAlreadyExist": mediaAlreadyExist.value,
        "NameMedia": pathMedia.value,
      };
      jsonMediaInfos = JSON.stringify(mediaInfos);
      return true
  }catch(error){
    console.error('Erreur lors de l attribution des données du média (json):', error.message);
    return false
  }
}

// Handle button click to start download
function handleConfirmClicked() {
  try {
    confirmClick.value = true;
    if (dataValid.value && torrentValid.value) {
      downloadingFlag.value = true // Set download state
      formattingJsonFile()
      if(sendDataToServer()){
        downloadSuceed.value = true
      }else{
        downloadError.value = true
      }
      downloadingFlag.value = false // End download
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

// Handle abort button click in ZoneDropFile component
function handleAbortZoneDropClicked(){
  resetTorrentFlag()
}

// Handle abort button click in ZoneFileInfo component
function handleAbortFileInfoClicked(){
  resetDataFlag()
}

// Reset confirm button value
function resetButtonValue() {
  confirmClick.value = false;
}

// Reset JSON data validity flag
function resetJsonDataValid(){
  dataValid.value = false
}

// Reset torrent validity flag
function resetTorrentFlag(){
  torrentValid.value = false
}

// Reset media data validity flag
function resetDataFlag(){
  dataValid.value = false
}

// Blink animation for indicating errors
function blinkdiv() {
  isBlinking.value = true;
  const durations = [200, 400, 600, 800, 1000];
  for (let i = 0; i < durations.length; i++) {
    setTimeout(() => {
      isBlinking.value = !isBlinking.value;
    }, durations[i]);
  }
}

// WebSocket message handler
ws.onmessage = (event) => {
  logMessages.value = [event.data]; // Replace current content with new message
};
</script>

<style scoped>
/**
 * Styles for main application container
 */
.myApp {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 60px;
}

/**
 * Styles for layout of ZoneDropFile and ZoneFileInfo components
 */
.twoZone {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 30px;
}

/**
 * Blink animation style
 */
.blink {
    outline: 2px solid var(--red-color-4); 
}

/**
 * Styles for button and spinner container
 */
.buttonAndSpinner {
  display: flex;
  flex-direction: row;
  align-items: center;
}

/**
 * Styles for hiding elements
 */
.noneVisible {
  display: none;
}
</style>
