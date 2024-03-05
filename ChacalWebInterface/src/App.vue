<!--
App.vue - Main Application Component

This component represents the main application layout and functionality.

Author: ChacalTordu
-->

<template>
  <div class="myApp">
    <div class="title"><p>Chacal Torrent</p></div>
      <div class="cards" >
          <cardTorrent @downloadClicked="handleDownloadClicked" v-for="(item, rowIndex) in componentList" :key="rowIndex"/>
      </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import cardTorrent from "./components/cardTorrent.vue";

const componentList = ref([cardTorrent]);
 
function handleDownloadClicked() {
  // console.log("callback handleDownloadClicked appelé")
  componentList.value.push(cardTorrent)
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
