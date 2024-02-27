<!--
ButtonSelectFile.vue - File Selection Button Component

This component defines a button used for selecting files. It allows users to choose files of a specific format.

Author: ChacalTordu
-->

<template>
  <label class="myButton" for="dropzoneFile">Select File</label>
  <input type="file" id="dropzoneFile" class="dropzoneFile" :accept="fileFormat" @change="handleFileSelect" />
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps(['fileFormat']);
const emit = defineEmits(['fileSelected']);

/**
* Handles file selection
* Emits 'fileSelected' event with selected file
*/
const handleFileSelect = (event) => {
  const files = event.target.files;
  if (files.length === 1 && files[0].name.endsWith(props.fileFormat)) {
      emit('fileSelected', files[0]);
      // console.log(`Valid ${props.fileFormat} file:`, files[0]);
  } else {
      alert(`Please select a ${props.fileFormat} file.`);
  }
};
</script>

<style scoped>
/**
* Button Styles
* Defines styles for the file selection button.
*/
.myButton {
  padding: 4px 20px;
  font-size: 16px;
  background-color: var(--green2-color-3);
  color: #ffffff;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

/**
* Button Hover Effect
* Defines hover effect for the file selection button.
*/
.myButton:hover {
  background-color:var(--green2-color-5);
}

/**
* Input Styles
* Hides the input element.
*/
input {
  display: none;
}
</style>
