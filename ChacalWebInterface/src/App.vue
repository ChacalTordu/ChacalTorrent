<!--
App.vue - Main Application Component

This component represents the main application layout and functionality.

Author: ChacalTordu
-->

<template>
  <div class="myApp">
    <div class="title"><p>Chacal Torrent</p></div>
      <div class="cards" >
          <cardTorrent @downloadClicked="handleDownloadClicked" v-for="(item, rowIndex) in componentList" :key="rowIndex" :item="item" ref="childComponent" />
      </div>
  </div>
</template>

<script setup>
  import { ref } from "vue";
  import cardTorrent from "./components/cardTorrent.vue";

  const socket = new WebSocket('ws://localhost:8080');
  const componentList = ref([cardTorrent]);

  function handleDownloadClicked(string_nameMedia) {
    componentList.value[componentList.value.length] = string_nameMedia;
  }

  socket.addEventListener('open', () => {
    console.log('Connexion WebSocket établie');
  });

  socket.addEventListener('message', (event) => {
    console.log('Événement reçu du serveur WebSocket:', event.data);
    handleMediaDownloaded(event.data);
  });

  function handleMediaDownloaded(blob) {
    blob.text().then(text => {
      const matchingComponent = componentList.value.find(item => item === text);
      if (matchingComponent) {
        console.log("Matching component found:", matchingComponent);
      } else {
        console.log("Media download but, no media match");
      }
    });
  }
</script>


<style scoped>
.myApp {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  gap: 60px;
}

.title {
  font-weight: bold;
  font-size: 75px;
  letter-spacing: 2px;
  color: #333;
  text-align: center;
}

.cards {
  display: flex;
  justify-content: center;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 80px;
}
</style>
