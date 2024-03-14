<template>
  <div class="myApp">
    <div class="title"><p>Chacal Torrent</p></div>
    <div class="cards">
      <cardTorrent @downloadClicked="handleDownloadClicked" v-for="(item, index) in componentList" :key="index" :mediaCardDownload="item.media" :bool_mediaDownload="item.bool_mediaDownload"/>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import cardTorrent from "./components/cardTorrent.vue";

const socket = new WebSocket('ws://localhost:8080');
const componentList = ref([]);

componentList.value.push({ media: '', bool_mediaDownload: false });

function handleDownloadClicked(string_nameMedia) {
  componentList.value[componentList.value.length - 1].media = string_nameMedia;
  componentList.value.push({ media: '', bool_mediaDownload: false });
}

socket.addEventListener('open', () => {
  console.log('Connexion WebSocket établie');
});

socket.addEventListener('message', (event) => {
  handleMediaDownloaded(event.data);
});

function handleMediaDownloaded(blob) {
  blob.text().then(text => {
    console.log("WebSocket received : ", text)
    const matchingIndex = componentList.value.findIndex(item => item.media === text);
    if (matchingIndex !== -1) {
      componentList.value[matchingIndex].bool_mediaDownload = true;
    }
  });
};
</script>

<style scoped>
.myApp {
  background-color: white;
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
