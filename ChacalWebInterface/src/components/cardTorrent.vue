<template>
    <div class="cardTorrent">
      <div class="content" :class="{ 'flipped': isFlipped }">
        <div class="front">
            <div class="frontContent">
                <div class="cardZoneFileInfo"><ZoneFileInfos /></div>
                <div class="cardZoneDropFile"><ZoneDropFile /></div>
                <div class="buttonDownload"><ButtonConfirm textButton="Télécharger"/></div>
            </div>
        </div>
        <div class="back">
          <div class="backContent">
  
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    import { ref } from 'vue';
    import ZoneFileInfos from './zone/ZoneFileInfos.vue';
    import ZoneDropFile from './zone/ZoneDropFile.vue';
    import ButtonConfirm from './button/ButtonConfirm.vue';
  
    const isFlipped = ref(false);
  
    const flipCard = () => {
      isFlipped.value = !isFlipped.value;
    };
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
    border-radius: 5px;
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
    border-radius: 5px;
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
    background-color: #ffffff; /* White background similar to Apple's card design */
    border-radius: 5px;
    color: black; /* Black text for better contrast */
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 30px;
  }
  
  .cardZoneFileInfo, .cardZoneDropFile {
      width: 90%;
      flex-basis: 180px;
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
  