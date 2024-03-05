<template>
  <div class="checkboxContainer">
    <div class="textCheckbox">{{ string_textQuestion }}</div>
    <div><ButtonToggleSlide @slideValueChanged="handleSlideValueChanged"/></div>
  </div>
</template>

<script setup>
import ButtonToggleSlide from '../button/ButtonToggleSlide.vue';

const props = defineProps({ string_textQuestion: String });
const emit = defineEmits(['slideValueChanged']);

function handleSlideValueChanged (bool_value) {
  emit('slideValueChanged', bool_value);
};

</script>

<style scoped>
.textCheckbox {
  flex: 1;
  font-size: 18px;
  color: var(--text-color-dark-2);
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
</style>
