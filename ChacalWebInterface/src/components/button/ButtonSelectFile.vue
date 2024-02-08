<template>
    <label class="myButton" for="dropzoneFile">Select File</label>
    <input type="file" id="dropzoneFile" class="dropzoneFile" :accept="fileFormat" @change="handleFileSelect" />
  </template>
  
  <script setup>
    import { defineProps, defineEmits } from 'vue';

    const props = defineProps(['fileFormat']);
    const emit = defineEmits();
  
    const handleFileSelect = (event) => {
      const files = event.target.files;
      if (files.length === 1 && files[0].name.endsWith(props.fileFormat)) {
        emit('fileSelected', files[0]);
        console.log(`Valid ${props.fileFormat} file:`, files[0]);
      } else {
        alert(`Please select a ${props.fileFormat} file.`);
      }
    };
  </script>
  
  <style scoped>
    .myButton {
      margin-top: 10px;
      padding: 4px 20px;
      font-size: 16px;
      background-color: var(--green2-color-4);
      color: #ffffff;
      border: none;
      border-radius: 30px;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }
  
    .myButton:hover {
      background-color:var(--green2-color-5);
    }
  
    input {
      display: none;
    }
  </style>
  