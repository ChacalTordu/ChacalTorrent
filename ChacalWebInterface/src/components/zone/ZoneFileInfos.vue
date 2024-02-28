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

const flag_dataValid = ref(false);

const string_title = ref();
const string_mediaType = ref();
const bool_includeSeveralSeason = ref();

let let_media = new class_MediaInfo(string_title, string_mediaType, bool_includeSeveralSeason);

function handleInputNameEntered(string_value){
  let_media.string_title = string_value;
  console.log("Titre :",test.string_title)
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
  console.log("Type de média: ",test.string_mediaType)
}

function handleSlideValueChanged(bool_value){
  let_media.bool_includeSeveralSeason = bool_value;
  console.log("Valeur slide:",bool_value)
}

// function handleConfirmClicked() {
//   if ((selectedMediaType.value === 'Film') || (selectedMediaType.value === 'Dessin animé')) {
//     if (pathMedia.value == '') {
//       emits('resetButton');
//     } else {
//       dataValidFlag.value = true;
//       emits('saveMediaData', selectedMediaType, pathMedia, false, false);
//     }
//   } else {
//     if ((checkbox1.value == undefined) || (checkbox2.value == undefined) || (pathMedia.value == '')) {
//       emits('resetButton');
//     } else {
//       dataValidFlag.value = true;
//       emits('saveMediaData', selectedMediaType, pathMedia, checkbox1.value, checkbox2.value);
//     }
//   }
// }

// function toggleInputTextVisible(value) {
//   if (value == "Yes") {
//     checkbox2.value = false;
//   } else if (value == "No") {
//     checkbox2.value = true;
//   }
// }

// function CheckCheckbox1Value(value) {
//   if (value == "Yes") {
//     checkbox1.value = true;
//   } else if (value == "No") {
//     checkbox1.value = false;
//   }
// }

// function toggleCheckbox1(value) {
//   CheckCheckbox1Value(value);
// }

// function CheckCheckbox2Value(value) {
//   if (value == "Yes") {
//     checkbox2.value = true;
//   } else if (value == "No") {
//     checkbox2.value = false;
//   }
// }

// function toggleCheckbox2(value) {
//   toggleInputTextVisible(value);
//   CheckCheckbox2Value(value);
// }

// function handleAbort() {
//   dataValidFlag.value = false;
//   emits('abortClicked');
// }
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

.myButton {
  width: 100px;
  height: 40px;
  margin: auto;
}
</style>
