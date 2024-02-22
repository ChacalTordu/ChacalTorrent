<!--
CheckboxTrueOrFalse.vue - Checkbox Component for True or False Options

This component defines a checkbox with two options: "Oui" (Yes) and "Non" (No). It emits a 'checkboxSet' event with the selected option.

Author: ChacalTordu
-->

<template>
  <div class="checkbox-container">
    <div class="textCheckbox">{{ textCheckbox }}</div>
    <div class="checkbox">
      <label :class="{ 'checked': checkbox1 }">
        <input type="checkbox" v-model="checkbox1" @change="handleCheckboxChange('checkbox1')"> Oui
      </label>
      <label :class="{ 'checked': checkbox2 }">
        <input type="checkbox" v-model="checkbox2" @change="handleCheckboxChange('checkbox2')"> Non
      </label>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({ textCheckbox: String });
const emit = defineEmits(['checkboxSet']);
const checkbox1 = ref(false);
const checkbox2 = ref(false);

/**
 * Handles checkbox change event
 * Emits 'checkboxSet' event with selected option
 */
const handleCheckboxChange = (checkbox) => {
  emit('checkboxSet');
  if (checkbox === 'checkbox1' && checkbox1.value) {
    checkbox2.value = false;
    emit('checkboxSet', "Yes");
  } else if (checkbox === 'checkbox2' && checkbox2.value) {
    checkbox1.value = false;
    emit('checkboxSet', "No");
  }
};
</script>

<style scoped>
/**
 * Checkbox Styles
 * Defines styles for the checkbox component.
 */
.textCheckbox {
  flex: 1;
  text-align: left;
}
.checkbox-container {
  width: 100%;
  height: 40px;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}
label {
  margin-right: 20px;
  cursor: pointer;
}
</style>
