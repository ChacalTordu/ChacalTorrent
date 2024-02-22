<template>
    <div class="loggerMessage">
      <div v-for="(message, index) in lastMessages" :key="index" class="loggerMessage">
        <p>{{ message }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps, computed } from 'vue';
  
  const props = defineProps({
    logMessages: {
      type: Array,
      required: true
    }
  });
  
  // Définir le nombre de derniers messages à afficher
  const maxMessages = 6;
  
  // Propriété calculée pour récupérer les derniers messages
  const lastMessages = computed(() => props.logMessages.slice(-maxMessages));
  </script>
    
  <style scoped>
  .loggerMessage {
    height: 160px; 
    width: 800px;
    background-color: var(--vt-c-divider-dark-2);
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;

    overflow-y: auto; /* Défilement vertical si la hauteur dépasse */
  }
  
  .loggerMessage p {
    margin: 0;
  }
  </style>
  