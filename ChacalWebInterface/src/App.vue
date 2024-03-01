<!--
App.vue - Main Application Component

This component represents the main application layout and functionality.

Author: ChacalTordu
-->

<template>
  <div class="myApp">
    <div class="title"><p>Chacal Torrent</p></div>
    <div class="cards"><cardTorrent /></div>
  </div>
</template>

<script setup>
import cardTorrent from "./components/cardTorrent.vue";
import { ref } from 'vue'

const ws = new WebSocket('ws://localhost:8080');
const logMessages = ref([]);

// WebSocket message handler
ws.onmessage = (event) => {
  logMessages.value = [event.data];
};
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
  flex-direction: row;
  gap: 80px;
}
</style>
