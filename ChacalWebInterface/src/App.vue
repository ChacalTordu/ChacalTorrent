<template>
  <div class="myApp">
    <div class="twoZone">
      <ZoneDropFile :confirmClicked="confirmClick" @fileChosen="saveTorrent" @resetButton="resetButtonValue"/>
      <ZoneFileInfo :confirmClicked="confirmClick" @saveMediaData="saveMediaInfo"  @resetButton="resetButtonValue"/>
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

  const dataValid = ref(false);
  const torrentValid = ref(false);
  
  const confirmClick = ref(false);

  const mediaType = ref('');
  const mediaMultipleSeason = ref(false);
  const mediaAlreadyExist = ref(false);
  const pathMedia = ref('');
  
  function handleConfirmClicked() {
    confirmClick.value = true;
    if (dataValid.value && torrentValid.value) {
      sendDataToServer();
    }
  }
  
  function resetButtonValue() {
    confirmClick.value = false;
  }
  
  async function sendDataToServer() {
    try {
      if (dataValid.value) {
        // console.log('Données FormData construites :');
        // console.log('mediaType:', mediaType.value);
        // console.log('multipleSeason:', mediaMultipleSeason.value);
        // console.log('alreadyExist:', mediaAlreadyExist.value);
        // console.log('NameMedia:', pathMedia.value);

        var mediaInfos = 
        {
          "mediaType" : mediaType.value,
          "boolMediaMultipleSeason" : mediaMultipleSeason.value,
          "boolAlreadyExist" : mediaAlreadyExist.value,
          "NameMedia" : pathMedia.value,
        }
        var jsonMediaInfos = JSON.stringify(mediaInfos)
        // console.log('JSON envoyé au serveur :', jsonMediaInfos);
      }
      axios.post('http://localhost:3000/uploadJSON', jsonMediaInfos)
        .then(response => {
          // console.log('Fichier téléchargé avec succès sur le serveur !');
        })
        .catch(error => {
          console.error('Erreur lors du téléchargement du fichier sur le serveur :', error);
        });
    } catch (error) {
      console.error('Une erreur est survenue :', error.message);
    }
  }

  function saveMediaInfo(saveMediaType, savePathMedia, saveCheckbox1, saveCheckbox2) {
    try {
        mediaType.value = saveMediaType.value;
        mediaMultipleSeason.value = saveCheckbox1;
        mediaAlreadyExist.value  = saveCheckbox2;
        pathMedia.value = savePathMedia.value;

        // Afficher les valeurs
        // console.log("mediaType:", mediaType.value);
        // console.log("mediaMultipleSeason:", mediaMultipleSeason.value);
        // console.log("mediaAlreadyExist:", mediaAlreadyExist.value);
        // console.log("pathMedia:", pathMedia.value);

        // Mettre à jour le drapeau de validation
        dataValid.value = true;
        sendDataToServer()
    } catch (error) {
        console.error('Une erreur est survenue lors de la sauvegarde des données du média:', error.message);
    }
}

  function saveTorrent(){
    torrentValid.value = true 
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
</style>