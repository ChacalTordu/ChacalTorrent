<template>
    <div class="group">      
      <input type="text">
      <span class="highlight"></span>
      <span class="bar"></span>
      <label>Titre</label>
    </div>
  </template>
  
  <script setup>
    
  </script>
  
  <style scoped>
  .group {
    position: relative;
    margin-bottom: 45px;
  }
  
  input {
    font-size: 18px;
    padding: 10px 10px 10px 5px;
    display: block;
    width: 300px;
    border: none;
    border-bottom: 1px solid #C8C6AF; /* Couleur gris clair */
    background-color: transparent; /* Fond transparent */
  }
  
  input:focus {
    outline: none;
  }
  
  label {
    color: #C8C6AF; /* Couleur gris clair */
    font-size: 18px;
    font-weight: normal;
    position: absolute;
    pointer-events: none;
    left: 5px;
    top: 10px;
    transition: 0.2s ease all;
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
  