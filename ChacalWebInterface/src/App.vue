<template>
  <div class="myApp">
    <div class="twoZone">
      <ZoneDropFile :class="{ 'blink': isBlinking && !torrentValid }" :confirmClicked="confirmClick" @fileChosen="saveTorrent" @resetButton="resetButtonValue"/>
      <ZoneFileInfo :class="{ 'blink': isBlinking && !dataValid }" :confirmClicked="confirmClick" @saveMediaData="saveMediaInfo"  @resetButton="resetButtonValue"/>
    </div>
    <ButtonConfirm textButton="Télécharger" @confirmClicked="handleConfirmClicked" />
  </div>
</template>

<script setup>
  import ZoneDropFile from "./components/ZoneDropFile.vue";
  import ZoneFileInfo from "./components/ZoneFileInfos.vue";
  import ButtonConfirm from "./components/button/ButtonConfirm.vue";
  import axios from 'axios';
  import { ref } from 'vue';

  const isBlinking = ref(false);

  const dataValid = ref(false);
  const torrentValid = ref(false);
  const fileTorrent = ref(null);
  
  const confirmClick = ref(false);

  const mediaType = ref('');
  const mediaMultipleSeason = ref(false);
  const mediaAlreadyExist = ref(false);
  const pathMedia = ref('');
  
  // Envoi le JSON et le fichier torrent au serveur
  async function sendDataToServer() {
    try {
      // Vérification du flag pour les données JSON
      if (dataValid.value) {
        const mediaInfos = {
          "mediaType": mediaType.value,
          "boolMediaMultipleSeason": mediaMultipleSeason.value,
          "boolAlreadyExist": mediaAlreadyExist.value,
          "NameMedia": pathMedia.value,
        };
        const jsonMediaInfos = JSON.stringify(mediaInfos);
        await axios.post('http://localhost:3000/uploadJSON', jsonMediaInfos);
        console.log('Json téléchargé avec succès sur le serveur !');
      }

      // Vérification du flag pour le fichier .torrent
      if (torrentValid.value && fileTorrent.value) {
        const formData = new FormData();
        formData.append('file', fileTorrent.value);
        await axios.post('http://localhost:3000/uploadFile', formData);
        console.log('Fichier téléchargé avec succès sur le serveur !');
      }  
    } catch (error) {
      console.error('Une erreur est survenue lors de l\'envoi des données au serveur:', error.message);
    }
  }

  function saveTorrent(file) {
    try {
      fileTorrent.value = file;
      // Flag à vrai
      torrentValid.value = true;
      console.log("Torrent sauvegardé correctement")
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
      // Flag à vrai
      dataValid.value = true;
    } catch (error) {
      console.error('Erreur lors de la sauvegarde des données du média (json):', error.message);
    }
  }

  function handleConfirmClicked() {
    try {
      confirmClick.value = true;
      if (dataValid.value && torrentValid.value) {
        sendDataToServer();
      }else{
        if (!dataValid.value) {
          blinkdiv('.ZoneFileInfo');
        } else if (!torrentValid.value) {
          blinkdiv('.ZoneDropFile');
        }
        console.log("Un des deux flags est à faux :\njson flag value :",dataValid.value,"\ntorrent flag value :",torrentValid.value)
      }
    } catch (error) {
      console.error('Une erreur est survenue lors du traitement du clic sur le bouton :', error.message);
    }
  }

  function resetButtonValue() {
    confirmClick.value = false;
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
</style>
