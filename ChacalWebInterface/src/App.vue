<template>
  <div class="myApp">
    <div class="twoZone">
      <ZoneDropFile :confirmClicked="confirmClick" @fileChosen="saveTorrent" @resetButton="resetButtonValue"/>
      <ZoneFileInfo :confirmClicked="confirmClick" @saveMediaData="saveDataMediaInfos" @saveMediaLessData='saveDataLessMediaInfos' @resetButton="resetButtonValue"/>
    </div>
    <ButtonConfirm textButton="Confirmez" @confirmClicked="handleConfirmClicked" />
  </div>
</template>

<script setup>
  import ZoneDropFile from "./components/ZoneDropFile.vue"
  import ZoneFileInfo from "./components/ZoneFileInfos.vue"
  import ButtonConfirm from "./components/button/ButtonConfirm.vue"
  import { ref } from 'vue'

  const confirmClick = ref(false)
  const dataValid = ref(false)
  const torrentValid = ref(false)
  const mediaType = ref('')
  const mediaMultipleSeason = ref(false)
  const mediaAlreadyExist = ref(false)
  const pathMedia = ref('')

  function handleConfirmClicked() {
    confirmClick.value = true
  }

  function resetButtonValue() {
    confirmClick.value = false
  }

  async function confirmData() {
    // // Vérification si toutes les données sont valides
    // if (dataValid.value && torrentValid.value) {
    //   try {
    //     const jsonData = {
    //       mediaType: mediaType.value,
    //       multipleSeason: mediaMultipleSeason.value,
    //       alreadyExist: mediaAlreadyExist.value,
    //       NameMedia : pathMedia.value
    //     };

    //     // Envoi des données au serveur
    //     axios.post('http://localhost:3000/upload', jsonData)
    //     .then(response => {
    //       console.log('Fichier téléchargé avec succès sur le serveur !');
    //     })
    //     .catch(error => {
    //       console.error('Erreur lors du téléchargement du fichier sur le serveur :', error);
    //     });

    //     if (response.ok) {
    //       console.log("Données envoyées avec succès !");
    //     } else {
    //       console.error("Erreur lors de l'envoi des données au serveur :", response.statusText);
    //     }
    //   } catch (error) {
    //     console.error("Une erreur est survenue lors de l'envoi des données au serveur :", error.message);
    //   }
    // } else {
    //   console.log("Il manque le torrent ou des informations sur le média.");
    // }
  }

  function saveDataLessMediaInfos(saveMediaType, savePathMedia) {
    mediaType.value = saveMediaType.value
    pathMedia.value = savePathMedia.value
    dataValid.value = true
    console.log("Voici toutes les infos", saveMediaType.value, savePathMedia.value)
    confirmData()
  }

  function saveDataMediaInfos(saveMediaType, saveCheckbox1, saveCheckbox2, savePathMedia) {
    mediaType.value = saveMediaType.value
    mediaMultipleSeason.value = saveCheckbox1
    mediaAlreadyExist.value = saveCheckbox2
    pathMedia.value = savePathMedia.value
    console.log("Voici toutes les infos :", saveMediaType.value, saveCheckbox1, saveCheckbox2, savePathMedia.value)
    dataValid.value = true
    confirmData()
  }

  function saveTorrent() {
    torrentValid.value = true
    confirmData()
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