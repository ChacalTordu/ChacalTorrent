<template>
  <div class="mediaContainer">
    <div><DivInputName @inputNameEntered="handleInputNameEntered"/></div>
    <div class="mediaType">
      <DivClickable class="divClickable" :class="{ 'mediaTypeSelected': bool_selected1 }" @divSelected="handleMediaTypeSelected" string_textDiv="Movie" />
      <DivClickable class="divClickable" :class="{ 'mediaTypeSelected': bool_selected2 }" @divSelected="handleMediaTypeSelected" string_textDiv="Cartoon" />
      <DivClickable class="divClickable" :class="{ 'mediaTypeSelected': bool_selected3 }" @divSelected="handleMediaTypeSelected" string_textDiv="Shows" />
      <DivClickable class="divClickable" :class="{ 'mediaTypeSelected': bool_selected4 }" @divSelected="handleMediaTypeSelected" string_textDiv="Anime" />
    </div>
    <div class="mediaChoice">
      <div class="seriesOptions">
        <div class="question">
          <DivQuestion @slideValueChanged="handleSlideValueChanged" string_textQuestion="Includes several seasons ?"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { class_MediaInfo } from '../../models/class_MediaInfo.js'
import DivInputName from '../div/DivInputName.vue';
import DivClickable from '../div/DivClickable.vue'
import DivQuestion from '../div/DivQuestion.vue';

const emits = defineEmits(['saveMediaInfos']);

const bool_selected1 = ref(null);
const bool_selected2 = ref(null);
const bool_selected3 = ref(null);
const bool_selected4 = ref(null);

let let_media = new class_MediaInfo('empty', 'empty', false);

function handleInputNameEntered(string_value){
  let_media.string_title = string_value;
  emits('saveMediaInfos',let_media)
}

function handleMediaTypeSelected(string_value) {
  switch (string_value) {
    case 'Movie':
      bool_selected1.value = true; 
      bool_selected2.value = false;
      bool_selected3.value = false;
      bool_selected4.value = false;
      break;
    case 'Cartoon':
      bool_selected1.value = false; 
      bool_selected2.value = true;
      bool_selected3.value = false;
      bool_selected4.value = false;
      break;
    case 'Shows':
      bool_selected1.value = false; 
      bool_selected2.value = false;
      bool_selected3.value = true;
      bool_selected4.value = false;
      break;
    case 'Anime':
      bool_selected1.value = false; 
      bool_selected2.value = false;
      bool_selected3.value = false;
      bool_selected4.value = true;
      break;
    default:
      break;
  }
  let_media.string_mediaType = string_value;
  // console.log("Type de média: ",let_media.string_mediaType)
  emits('saveMediaInfos',let_media)
}

function handleSlideValueChanged(bool_value){
  let_media.bool_includeSeveralSeason = bool_value;
  emits('saveMediaInfos',let_media)
}
</script>

<style scoped>
.mediaContainer {
  margin: auto;
  display: grid;
  padding: 10px;
}

.mediaType {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}

.divClickable {
  width: auto;
  background: #e8e8e8; 
  border-radius: 5px;
  padding: 0px 10px 0px 10px;
}

.mediaTypeSelected {
  background-color: #007aff; /* Apple-like blue color */
  color: white; /* White text for better contrast */
}

.mediaChoice {
  width: 99%;
  display: block;
  flex-direction: column;
  align-items: center;
}

input {
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  box-sizing: border-box;
}

input:hover,
input:focus {
  border-color: #007aff; /* Apple-like blue color */
}

.question {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
