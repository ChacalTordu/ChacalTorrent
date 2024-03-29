<!--
ZoneDropFile.vue - File Drop Zone Component

This component defines a drop zone for uploading files. It allows users to drag and drop files or select them using a button.

Author: ChacalTordu
-->

<template>
  <div 
    @dragenter.prevent="handleDragEnter"
    @dragleave.prevent="handleDragLeave"
    @dragover.prevent
    @drop.prevent="handleDrop"
    class="dropzone"
    :class="{'activeDropzone': active , 'hasFile': hasFile}">
    <span v-if="!hasFile">Drag or Drop or Select File</span>
    <ButtonSelectFile v-if="!hasFile" fileFormat=".torrent" @fileSelected="handleFileSelected"/>
    <span v-if="hasFile">{{ fileName }}</span>
    <ButtonAbort v-if="hasFile" textButton="Annuler" @abort="handleAbort"/>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import ButtonSelectFile from '../button/ButtonSelectFile.vue';
import ButtonAbort from '../button/ButtonAbort.vue';

const acceptedFormat = ".torrent";

const active = ref(false);
const hasFile = ref(false);
const fileName = ref('');

const emits = defineEmits(['fileChosen','fileAbort']);

  // # *****************************************************************************************************************
  // # *****************************************************************************************************************
  // # H A N D L E   F U N C T I O N S          
  // # *****************************************************************************************************************
  // # *****************************************************************************************************************

  function handleDragEnter(event) {
    event.preventDefault();
    active.value = true;
  }

  function handleDragLeave() {
    active.value = false;
  }

  function handleDrop(event) {
    event.preventDefault();
    active.value = false;
    const files = event.dataTransfer.files;
    if (files.length !== 1) {
      alert("Veuillez ne déposer qu'un seul fichier.");
    } else if (checkFileFormat(files[0])) {
      alert(`Veuillez sélectionner un fichier ${acceptedFormat}.`);
    } else {
      handleFileSelected(files[0]);
    }
  }

  function handleFileSelected(file) {
    if (checkFileFormat(file)) {
      alert(`Veuillez sélectionner un fichier ${acceptedFormat}.`);
    } else {
      hasFile.value = true;
      fileName.value = file.name;
      emits('fileChosen', file);
    }
  }

  function handleAbort() {
    try {
      hasFile.value = false;
      fileName.value = '';
      emits('fileAbort');
    } catch (error) {
      console.error("Une erreur est survenue:", error);
    }
  }

  // # *****************************************************************************************************************
  // # *****************************************************************************************************************
  // # M I N O R   F U N C T I O N S          
  // # *****************************************************************************************************************
  // # *****************************************************************************************************************

  function checkFileFormat(file) {
    const fileExtension = file.name.split('.').pop();
    return fileExtension.toLowerCase() === acceptedFormat.toLowerCase();
  }
</script>

<style scoped>
/**
 * Dropzone Styles
 */
.dropzone {
  height: 57px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  text-align: center;
  font-size: 16px;
  color: #666;
  padding: 10px;
  border: 2px dashed #ccc;
  transition: background-color 0.3s ease-in-out;
  gap: 15px;
  border-radius: 10px;

  /* max-width: 300px; Ajustez cette valeur selon vos besoins */
  white-space: nowrap; /* Empêche le texte de se mettre à la ligne */
  overflow: hidden; /* Cache tout texte qui dépasse la limite */
  text-overflow: ellipsis; /* Ajoute des points de suspension si le texte est coupé */

}

/**
 * Active Dropzone Styles
 */
.activeDropzone {
  background-color: #f0f0f0;
}
span {
  max-width: 250px;
}
/**
 * File Present Styles
 */
.hasFile {
  border-style: solid;
  display: flex;
}
.hasFile .ButtonAbort {
  flex: 1; /* Fait en sorte que le bouton "Abort" s'étende pour remplir l'espace disponible */
  max-width: 50px; /* Limite la largeur maximale du bouton */
}
</style>
