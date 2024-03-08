<template>
  <div class="group">      
    <input type="text" v-model="inputValue" @keyup.enter="emitInputValue" @blur="emitInputValue" placeholder="Title">
    <span class="highlight"></span>
    <span class="bar"></span>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const emit = defineEmits(['inputNameEntered']);
const inputValue = ref('');

const emitInputValue = () => {
  document.activeElement.blur();
  emit('inputNameEntered',inputValue.value);
}
</script>

  <style scoped>
  .group {
    position: relative;
    margin-bottom: 15px;
  }
  
  input {
    font-size: 18px;
    padding: 10px 10px 10px 5px;
    display: block;
    width: 300px;
    border: none;
    border-bottom: 2px solid var(--background-color-light);
  }
  
  input:focus {
    outline: none;
  }
  
  input:focus ~ label,
  input:valid ~ label {
    top: -20px;
    font-size: 14px;
    color: #C8C6AF; /* Couleur gris clair */
  }
  
  .bar {
    position: relative;
    display: block;
    width: 300px;
  }
  
  .bar:before,
  .bar:after {
    content: '';
    height: 2px;
    width: 0;
    bottom: 1px;
    position: absolute;
    background: #C8C6AF; /* Couleur gris clair */
    transition: 0.2s ease all;
  }
  
  .bar:before {
    left: 50%;
  }
  
  .bar:after {
    right: 50%;
  }
  
  input:focus ~ .bar:before,
  input:focus ~ .bar:after {
    width: 50%;
  }
  
  .highlight {
    position: absolute;
    height: 60%;
    width: 100px;
    top: 25%;
    left: 0;
    pointer-events: none;
    opacity: 0.5;
  }
  
  input:focus ~ .highlight {
    -webkit-animation: inputHighlighter 0.3s ease;
    animation: inputHighlighter 0.3s ease;
  }
  
  @keyframes inputHighlighter {
    from { background: #C8C6AF; } /* Couleur gris clair */
    to { width: 0; background: transparent; }
  }
  </style>
  