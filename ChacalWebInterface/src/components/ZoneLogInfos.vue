<!--
ZoneLogInfos.vue - Log Information Component

This component displays log messages with formatting options.

Author: ChacalTordu
-->

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
  
  // Define the number of last messages to display
  const maxMessages = 6;
  
  // Computed property to retrieve the last messages
  const lastMessages = computed(() => props.logMessages.slice(-maxMessages));
  
  // Function to format messages with line breaks
  function formatMessage(message) {
    return message.replace(/\n/g, '<br>');
  }
  </script>
  
  <style scoped>
  /**
   * Styles for Logger Message container
   */
  .loggerMessage {
    height: 160px; 
    width: 900px;
    background-color: var(--vt-c-text-dark-2);
    border-radius: 5px;
    padding: 10px;
    box-shadow: 0.5px 2px 1px rgba(0, 0, 0, 0.2);
    overflow-y: auto; /* Vertical scrolling if height exceeds */
  }
  
  /**
   * Styles for individual messages
   */
  .messages {
    margin-bottom: 10px;
  }
  
  /**
   * Styles for Logger Message paragraphs
   */
  .loggerMessage p {
    margin: 0;
    white-space: pre-wrap; /* Preserve line breaks */
  }
  </style>
  