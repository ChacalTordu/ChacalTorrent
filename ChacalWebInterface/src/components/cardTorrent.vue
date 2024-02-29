<template>
    <div class="cardTorrent">
      <div class="content" :class="{ 'flipped': bool_isFlipped }">
        <div class="front">
            <div class="frontContent">
                <div class="cardZoneFileInfo"><ZoneFileInfos @saveMediaInfos="handleSaveMediaInfos"/></div>
                <div class="cardZoneDropFile"><ZoneDropFile @fileChosen="handleSaveTorrent" @fileAbort="handleTorrentAbort"/></div>
                <div class="buttonDownload"><ButtonConfirm @confirmClicked="handleConfirmClicked" textButton="Download"/></div>
                <div :class="{ 'nonVisible': !bool_flagErrorMessage }" style="color: red;">Please enter all required values</div>
            </div>
        </div>
        <div class="back">
          <div class="backContent">
            <div><Spinner/></div>
            <div><Error/></div>
            <div><Success/></div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    import { ref } from 'vue';
    import axios from 'axios'

    import { class_MediaInfo } from '@/models/class_MediaInfo';
    import ZoneFileInfos from './zone/ZoneFileInfos.vue';
    import ZoneDropFile from './zone/ZoneDropFile.vue';
    import ButtonConfirm from './button/ButtonConfirm.vue';
    import Spinner from './animation/Spinner.vue';
    import Error from './animation/Error.vue';
    import Success from './animation/Success.vue';

    var jsonMediaInfos
    
    let let_newMediaInfo = new class_MediaInfo();
    const formData_formData = new FormData();
    
    const bool_flagErrorMessage = ref(false)
    const bool_isFlipped = ref(false);
    const file_fileTorrent = ref(null)

    // # *****************************************************************************************************************
    // # *****************************************************************************************************************
    // # H A N D L E   F U N C T I O N S          
    // # *****************************************************************************************************************
    // # *****************************************************************************************************************

    function handleSaveMediaInfos(let_mediaInfos) {
      let_newMediaInfo.string_title = let_mediaInfos.string_title;
      let_newMediaInfo.string_mediaType = let_mediaInfos.string_mediaType;
      let_newMediaInfo.bool_includeSeveralSeason = let_mediaInfos.bool_includeSeveralSeason;
    }

    function handleSaveTorrent(file_torrent) {
      try {
        file_fileTorrent.value = file_torrent;
        formData_formData.set('file', file_fileTorrent.value);
      } catch(error) {
        console.error('Erreur lors de la sauvegarde des données du fichier .torrent:', error.message);
      }
    }

    function handleTorrentAbort() {
      file_fileTorrent.value = null;
    }

    function handleConfirmClicked() {
      // Verification des données - Création du json associés au infos - Envoie des données au serveur
      if(validateMediaInfo(let_newMediaInfo)){
        if(validateTorrent()){
          if(formattingJsonFile()){
            bool_isFlipped.value = true;
            if(sendDataToServer()){ 
            }else{bool_flagErrorMessage.value = true}
          }else{bool_flagErrorMessage.value = true;return}
        }else{bool_flagErrorMessage.value = true;return}
      }else{bool_flagErrorMessage.value = true;return}
    }

    // # *****************************************************************************************************************
    // # *****************************************************************************************************************
    // # M I N O R   F U N C T I O N S          
    // # *****************************************************************************************************************
    // # *****************************************************************************************************************

    // Fonction de validation des attributs de let_newMediaInfo
    function validateMediaInfo(let_mediaInfo) {
      // Vérification du titre
      if (!let_mediaInfo.string_title || typeof let_mediaInfo.string_title !== 'string') {
        console.error("Titre invalide");
        return false
      }

      // Vérification du type de média
      if (!let_mediaInfo.string_mediaType || !['Movie', 'Cartoon', 'Shows', 'Anime'].includes(let_mediaInfo.string_mediaType)) {
        console.error("Type de média invalide");
        return false
      }

      // Vérification de la présence de plusieurs saisons
      if (let_mediaInfo.bool_includeSeveralSeason.value !== true && let_mediaInfo.bool_includeSeveralSeason.value !== false) {
        console.error("La valeur d'inclusion de plusieurs saisons est invalide");
        return false;
      }

      return true
    }

    // Fonction de vaidation du torrent entré
    function validateTorrent() {
      if (file_fileTorrent.value != null){
        return true
      }else{
        return false
      }
    }

    // Format JSON file
    function formattingJsonFile() {
      try{
        var mediaInfos = {
            "NameMedia": let_newMediaInfo.string_title,
            "mediaType": let_newMediaInfo.string_mediaType,
            "boolMediaMultipleSeason": let_newMediaInfo.bool_includeSeveralSeason,
            "boolAlreadyExist": false,
          };
          jsonMediaInfos = JSON.stringify(mediaInfos);
          return true
      }catch(error){
        console.error('Erreur lors de l attribution des données du média (json):', error.message);
        return false
      }
    }

    // Send JSON and torrent file to server
    function sendDataToServer() {
      try {
        axios.post('http://localhost:3000/uploadFile', formData_formData);
        console.log('Fichier téléchargé avec succès sur le serveur !');
        axios.post('http://localhost:3000/uploadJSON', jsonMediaInfos);
        console.log('Json téléchargé avec succès sur le serveur !');
        return true
      } catch (error) {
        console.error('Une erreur est survenue lors de l\'envoi des données au serveur:', error.message);
        return false
      }
    }
  </script>
  
  <style scoped>
  .cardTorrent {
    overflow: visible;
    width: 400px;
    height: 520px;
    perspective: 1000px;
    background-color: #f4f4f4; /* Background color similar to Apple's light gray */
  }

  .content {
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    transition: transform 300ms;
    box-shadow: 0px 0px 10px 1px #000000ee;
    border-radius: 15px;
  }

  .cardZoneFileInfo, .cardZoneDropFile {
      width: 90%;
  }
  
  .content.flipped {
    transform: rotateY(180deg);
  }
  
  .front {
    background-color: #ffffff; /* White background similar to Apple's card design */
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    border-radius: 15px;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .front::before {
    position: absolute;
    content: ' ';
    display: block;
    width: 160px;
    height: 160%;
    background: linear-gradient(90deg, transparent, #007aff, #007aff, #007aff, #007aff, transparent); /* Gradient similar to Apple's blue color */
    animation: rotation_481 5000ms infinite linear;
  }
  
  .frontContent {
    position: absolute;
    width: 99%;
    height: 99%;
    background-color: #ffffff;
    border-radius: 15px;
    color: black;
    display: flex;
    flex-direction: column;
    align-items: center;
    z-index: 3;
  }

  .backContent {
    position: absolute;
    z-index: 2;
  }
  

  .buttonDownload {
    margin-top: auto;
    margin-bottom: 10px;
  }

  .nonVisible {
    display: none;
  }
  
  @keyframes rotation_481 {
    0% {
      transform: rotateZ(0deg);
    }
  
    100% {
      transform: rotateZ(360deg);
    }
  }
  </style>
  