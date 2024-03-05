<template>
  <label class="switch">
    <input type="checkbox" v-model="bool_checked" @change="handleSlideValueChanged">
    <span class="slider"></span>
  </label>
</template>

<script setup>
import { ref } from 'vue';

const bool_checked = ref(false);

const emits = defineEmits(['slideValueChanged']);

function handleSlideValueChanged() {
  emits('slideValueChanged', bool_checked.value);
}
</script>
  
  <style scoped>
  .switch {
    position: relative;
    display: inline-block;
    width: 40px; /* Réduction de la largeur */
    height: 24px; /* Réduction de la hauteur */
  }
  
  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  
  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #c4c4c4; /* Couleur de fond */
    -webkit-transition: .4s;
    transition: .4s;
    border-radius: 12px; /* Arrondi des coins */
  }
  
  .slider:before {
    position: absolute;
    content: "";
    height: 16px; /* Réduction de la hauteur */
    width: 16px; /* Réduction de la largeur */
    left: 4px;
    bottom: 4px;
    background-color: white;
    -webkit-transition: .4s;
    transition: .4s;
    border-radius: 50%;
  }
  
  input:checked + .slider {
    background-color: #007aff; /* Couleur de fond lorsque le bouton est activé */
  }
  
  input:focus + .slider {
    box-shadow: 0 0 1px #007aff; 
  }
  
  input:checked + .slider:before {
    -webkit-transform: translateX(16px); /* Déplacement du curseur lorsqu'il est activé */
    -ms-transform: translateX(16px);
    transform: translateX(16px);
  }
  
  /* Style du bouton arrondi */
  .slider {
    border-radius: 12px;
  }
  
  .slider:before {
    border-radius: 50%;
  }
  </style>
  