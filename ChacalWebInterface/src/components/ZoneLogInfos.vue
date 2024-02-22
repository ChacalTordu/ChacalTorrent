<template>
    <div class="loggerMessage">
      <div v-for="(message, index) in lastMessages" :key="index" class="messages">
        <p v-html="formatMessage(message)"></p>
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
  
  // Fonction pour formater les messages avec les sauts de ligne
  function formatMessage(message) {
    return message.replace(/\n/g, '<br>');
  }
  </script>
  
  <style scoped>
  .loggerMessage {
    height: 160px; 
    width: 900px;
    background-color: var(--vt-c-text-dark-2);
    border-radius: 5px;
    padding: 10px;
    box-shadow: 0.5px 2px 1px rgba(0, 0, 0, 0.2);
    overflow-y: auto; /* Défilement vertical si la hauteur dépasse */
  }
  
  .messages {
    margin-bottom: 10px;
  }
  
  .loggerMessage p {
    margin: 0;
    white-space: pre-wrap; /* Préserver les sauts de ligne */
  }
  </style>
  