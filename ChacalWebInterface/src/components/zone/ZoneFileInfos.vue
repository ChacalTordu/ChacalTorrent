<template>
  <div class="mediaContainer" :class="{ 'dataValid': dataValidFlag }">
    <div><InputName /></div>
    <div class="mediaType">
      <DivClickable class="divClickable" :class="{ 'mediaTypeSelected': selected1 }" @divSelected="handleMediaTypeSelected" textDiv="Film" />
      <DivClickable class="divClickable" :class="{ 'mediaTypeSelected': selected2 }" @divSelected="handleMediaTypeSelected" textDiv="DessinAnimé" />
      <DivClickable class="divClickable" :class="{ 'mediaTypeSelected': selected3 }" @divSelected="handleMediaTypeSelected" textDiv="Série" />
      <DivClickable class="divClickable" :class="{ 'mediaTypeSelected': selected4 }" @divSelected="handleMediaTypeSelected" textDiv="Animé" />
    </div>

    <div class="mediaChoice">
      <div class="seriesOptions">
        <div class="question">
          <CheckboxTrueOrFalse @checkboxSet="toggleCheckbox1" textCheckbox="Contient plusieurs saison ?"/>
          <CheckboxTrueOrFalse @checkboxSet="toggleCheckbox2" textCheckbox="Média déjà existant ?"/>
          <input v-if="checkbox2" v-model="pathMedia" placeholder="Recherchez le dossier :" disabled>
          <p v-if="checkbox2" style="text-align: center; margin-top: 5px; color: #f00;">Fonctionnalité pas encore disponible. Veuillez télécharger le .torrent manuellement et le placer correctement dans le serveur.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue';
import InputName from '../div/InputName.vue';
import DivClickable from '../div/DivClickable.vue'
import CheckboxTrueOrFalse from '../checkbox/CheckboxTrueOrFalse.vue';

const dataValidFlag = ref(false);
const selectedMediaType = ref('Nom du média');
const pathMedia = ref('');
const checkbox1 = ref();
const checkbox2 = ref();
const selected1 = ref(null);
const selected2 = ref(null);
const selected3 = ref(null);
const selected4 = ref(null);

const emits = defineEmits(['saveMediaData', 'resetButton', 'abortClicked']);

function handleMediaTypeSelected(textDiv) {
  selectedMediaType.value = textDiv;
  switch (textDiv) {
    case 'Film':
      selected1.value = true; 
      selected2.value = false;
      selected3.value = false;
      selected4.value = false;
      break;
    case 'DessinAnimé':
      selected1.value = false; 
      selected2.value = true;
      selected3.value = false;
      selected4.value = false;
      break;
    case 'Série':
      selected1.value = false; 
      selected2.value = false;
      selected3.value = true;
      selected4.value = false;
      break;
    case 'AnimeJaponais':
      selected1.value = false; 
      selected2.value = false;
      selected3.value = false;
      selected4.value = true;
      break;
    default:
      break;
  }
}

function handleConfirmClicked() {
  if ((selectedMediaType.value === 'Film') || (selectedMediaType.value === 'Dessin animé')) {
    if (pathMedia.value == '') {
      emits('resetButton');
    } else {
      dataValidFlag.value = true;
      emits('saveMediaData', selectedMediaType, pathMedia, false, false);
    }
  } else {
    if ((checkbox1.value == undefined) || (checkbox2.value == undefined) || (pathMedia.value == '')) {
      emits('resetButton');
    } else {
      dataValidFlag.value = true;
      emits('saveMediaData', selectedMediaType, pathMedia, checkbox1.value, checkbox2.value);
    }
  }
}

function toggleInputTextVisible(value) {
  if (value == "Yes") {
    checkbox2.value = false;
  } else if (value == "No") {
    checkbox2.value = true;
  }
}

function CheckCheckbox1Value(value) {
  if (value == "Yes") {
    checkbox1.value = true;
  } else if (value == "No") {
    checkbox1.value = false;
  }
}

function toggleCheckbox1(value) {
  CheckCheckbox1Value(value);
}

function CheckCheckbox2Value(value) {
  if (value == "Yes") {
    checkbox2.value = true;
  } else if (value == "No") {
    checkbox2.value = false;
  }
}

function toggleCheckbox2(value) {
  toggleInputTextVisible(value);
  CheckCheckbox2Value(value);
}

function handleAbort() {
  dataValidFlag.value = false;
  emits('abortClicked');
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
  background: #e8e8e8; /* Apple-like gray background */
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
