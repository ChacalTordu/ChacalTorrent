<template>
  <div 
    @dragenter.prevent="handleDragEnter"
    @dragleave.prevent="handleDragLeave"
    @dragover.prevent
    @drop.prevent="handleDrop"
    :class="{ 'activeDropzone': active , 'hasFile': hasFile, 'blink': isBlinking}"
    class="dropzone">
    <span v-if="!hasFile">Drag or Drop File</span>
    <span v-if="!hasFile">OR</span>
    <ButtonSelectFile v-if="!hasFile" fileFormat=".torrent" @fileSelected="handleFileSelected"/>
    <span v-if="hasFile">{{ fileName }}</span>
    <ButtonAbort v-if="hasFile" textButton="Annuler" @abort="handleAbort"/>
  </div>
</template>

<script setup>
import ButtonSelectFile from './button/ButtonSelectFile.vue'
import ButtonAbort from './button/ButtonAbort.vue'
import { ref, watch } from "vue"
import axios from 'axios'

const active = ref(false);
const acceptedFormat = '.torrent';
const hasFile = ref(false);
const fileName = ref('')
const props = defineProps({
  confirmClicked: Boolean
});
const isBlinking = ref(false);
const emits = defineEmits(['resetButton','fileChosen']) 

const handleDragEnter = (event) => {
  event.preventDefault();
  active.value = true;
};

const handleDragLeave = () => {
  active.value = false;
};

const handleDrop = (event) => {
  event.preventDefault()
  active.value = false
  const files = event.dataTransfer.files
  if (checkFileFormat(files[0])) {
    alert(`Please select a ${acceptedFormat} file.`)
  } else {
    uploadFile(files[0])
  }
};

const handleFileSelected = (file) => {
  hasFile.value = true
  fileName.value = file.name
  emits('fileChosen')
  uploadFile(file)
};

const checkFileFormat = (file) => {
  return file.type === acceptedFormat
};

const handleAbort = () => {
  try {
    hasFile.value = false
    fileName.value = ''
    console.log("File aborted successfully")
  } catch (error) {
    console.error("An error occurred:", error);
  }
};

const uploadFile = (file) => {
  const formData = new FormData();
  formData.append('file', file);

  axios.post('http://localhost:3000/upload', formData)
    .then(response => {
      console.log('Fichier téléchargé avec succès sur le serveur !');
    })
    .catch(error => {
      console.error('Erreur lors du téléchargement du fichier sur le serveur :', error);
    });
}

function blinkdiv() {
  isBlinking.value = true;
  const durations = [200, 400, 600, 800, 1000];
  for (let i = 0; i < durations.length; i++) {
    setTimeout(() => {
      isBlinking.value = !isBlinking.value;
    }, durations[i]);
  }
}

watch(() => props.confirmClicked, () => {
  if (props.confirmClicked == true) {
    if(hasFile.value == false){
      blinkdiv()
      emits('resetButton')
    }
  }
});
</script>

<style scoped>
.dropzone {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 400px;
  height: 200px;
  border: 2px dashed #ccc;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
  text-align: center;
  font-size: 16px;
  color: #666;
  padding: 10px;
  transition: background-color 0.3s ease-in-out;
}

.dropzone span {
  margin-bottom: 10px;
}

.activeDropzone {
  background-color: #f0f0f0;
}

.hasFile {
  border-style: solid;
}

.blink {
    outline: 2px solid var(--red-color-4); 
    border: none;
  }
</style>
