<template>
  <div :class="{ 'blink': isBlinking }" class="mediaContainer">
    <div class="mediaType">
      <label class="mediaLabel" for="movie">
        <input class="radio" type="radio" id="movie" value="Film" v-model="selectedMediaType">
        <span>Film</span>
      </label>

      <label class="mediaLabel" for="cartoon">
        <input class="radio" type="radio" id="cartoon" value="Dessin animé" v-model="selectedMediaType">
        <span>Dessin Animé</span>
      </label>

      <label class="mediaLabel" for="shows">
        <input class="radio" type="radio" id="shows" value="Série" v-model="selectedMediaType">
        <span>Série</span>
      </label>

      <label class="mediaLabel" for="animeJap">
        <input class="radio" type="radio" id="animeJap" value="Anime Japonais" v-model="selectedMediaType">
        <span>Animé Japonais</span>
      </label>
    </div>

    <div class="mediaChoice">
      <div v-if="selectedMediaType === 'Film' || selectedMediaType === 'Dessin animé'" class="seriesOptions">
        <input v-model="pathMedia" placeholder="Entrez le nom du média ici">
      </div>
      <div v-if="selectedMediaType === 'Série' || selectedMediaType === 'Anime Japonais'" class="seriesOptions">
        <div class="question">
          <CheckboxTrueOrFalse @checkboxSet="toggleCheckbox1" textCheckbox="Contient plusieurs saison ?"/>
          <CheckboxTrueOrFalse @checkboxSet="toggleCheckbox2" textCheckbox="Média déjà existant ?"/>
          <input v-if="!checkbox2" v-model="pathMedia" placeholder="Entrez le nom du média ici">
          <!-- <input v-if="checkbox2" v-model="pathMedia" placeholder="Entrez le chemin du média ici (commençant par '/')"> -->
          <input v-if="checkbox2" v-model="pathMedia" placeholder="Recherchez le dossier :" disabled>
          <p v-if="checkbox2" style="text-align: center; margin-top: 5px; color: #f00;">Fonctionnalité pas encore disponible. Veuillez télécharger le .torrent manuellement et le placer correctement dans le serveur.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import CheckboxTrueOrFalse from './checkbox/CheckboxTrueOrFalse.vue'

const selectedMediaType = ref('Nom du média')
const pathMedia = ref('')
const checkbox1 = ref()
const checkbox2 = ref()
const isBlinking = ref(false);

const props = defineProps({
  confirmClicked: Boolean
});

const emits = defineEmits(['saveMediaData','resetButton'])

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
    if ((selectedMediaType.value === 'Film') || (selectedMediaType.value === 'Dessin animé') ) {
      if (pathMedia.value == '') {
        blinkdiv()
        emits('resetButton')
      }else{
        emits('saveMediaData',selectedMediaType,pathMedia,false,false)
      }
    }else{
      if((checkbox1.value == undefined) || (checkbox2.value == undefined) || (pathMedia.value == '')){
      blinkdiv()
      emits('resetButton')
    }else{
      emits('saveMediaData',selectedMediaType,pathMedia,checkbox1.value,checkbox2.value)
    }
    }
  }
});

function toggleInputTextVisible(value){
  if (value == "Yes") {
    checkbox2.value = false
  } else if (value == "No") {
    checkbox2.value = true
  }
}

function CheckCheckbox1Value(value){
  if (value == "Yes") {
    checkbox1.value = true
  } else if (value == "No") {
    checkbox1.value = false
  }
}

function toggleCheckbox1(value){
  CheckCheckbox1Value(value)
}

function CheckCheckbox2Value(value){
  if (value == "Yes") {
    checkbox2.value = true
  } else if (value == "No") {
    checkbox2.value = false
  }
}

function toggleCheckbox2(value){
  toggleInputTextVisible(value)
  CheckCheckbox2Value(value)
}

</script>

<style scoped>
  .mediaContainer {
    width: 600px;
    margin: auto;
    display: grid;
    border-radius: 8px;
    padding: 10px;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.2);
  }
  .blink {
    outline: 2px solid var(--red-color-4); 
  }
  .mediaType {
    display: flex;
    flex-direction:row;
    justify-content: space-around;
  }

  .mediaLabel {
    align-items: center;
    margin-bottom: 10px;
    cursor: pointer;
  }

  .mediaLabel span {
    margin-left: 16px;
  }

  .mediaChoice {
    width: 100%;
    display: block;
    flex-direction: column;
    align-items: center;
  }

  p {
    text-align: center;
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
    border-color: #C8C6AF;
  }

  .seriesOptions {
    display: flex;
    flex-direction: row;
    align-items: center;
  }

  .question {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>
