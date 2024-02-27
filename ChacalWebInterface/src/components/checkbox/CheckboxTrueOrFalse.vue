<template>
  <div class="checkboxContainer">
    <div class="textCheckbox">{{ textCheckbox }}</div>
    <input type="checkbox" id="switch" v-model="checked" @change="handleChange" />
    <label for="switch"></label>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({ textCheckbox: String });
const emit = defineEmits(['checkboxSet']);
const checked = ref(false);

const handleChange = () => {
  emit('checkboxSet', checked.value ? 'Yes' : 'No');
};
</script>

<style scoped>
.textCheckbox {
  flex: 1;
  text-align: left;
}
.checkboxContainer {
  width: 100%;
  height: 40px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}

input[type=checkbox]{
  height: 0;
  width: 0;
  visibility: hidden;
}

label {
  cursor: pointer;
  text-indent: -9999px;
  width: 40px;              /* Réduire la taille du toggle switch */
  height: 20px;             /* Réduire la taille du toggle switch */
  background: grey;
  display: block;
  border-radius: 20px;      /* Ajuster la bordure arrondie */
  position: relative;
}

label:after {
  content: '';
  position: absolute;
  top: 2px; /* Ajuster la position verticale */
  left: 2px; /* Ajuster la position horizontale */
  width: 16px; /* Ajuster la taille du bouton */
  height: 16px; /* Ajuster la taille du bouton */
  background: #fff;
  border-radius: 50%; /* Rendre le bouton rond */
  transition: 0.3s;
}

input:checked + label {
  background: #5cda5c;
}

input:checked + label:after {
  left: calc(100% - 2px);
  transform: translateX(-100%);
}

label:active:after {
  width: 20px; /* Ajuster la taille du bouton lorsqu'il est activé */
}
</style>
