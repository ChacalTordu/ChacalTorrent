<!--
App.vue - Main Application Component

This component represents the main application layout and functionality.

Author: ChacalTordu
-->

<template>
  <div class="myApp">
    <div class="title"><p>Chacal Torrent</p></div>
      <div class="cards">
        <div class="cardsRow" v-for="(row, index) in componentRows" :key="index">
          <div v-for="(item, rowIndex) in componentList" :key="rowIndex" class="cardItem">
            <cardTorrent @downloadClicked="handleDownloadClicked"/>
          </div>
        </div>
      </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import cardTorrent from "./components/cardTorrent.vue";

const componentList = ref([cardTorrent]);
 
function handleDownloadClicked() {
  console.log("callback handleDownloadClicked appelé")
  componentList.value.push(cardTorrent)
}

const componentRows = computed(() => {
  const rows = [];
  const components = componentList.value;
  const numComponent = components.length;
  
  let rowIndex = 0;

  for (let i = 0; i < numComponent; i+=3) {
    rows.push(components.slice(i,i+3));
  }
  return rows;

});

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
  flex-wrap: wrap;
}

.cardsRow {
  display: flex;
  flex-wrap: wrap;
  /* gap: 80px; */
  margin-bottom: 20px;
}
</style>
