<!--
ButtonConfirm.vue - Confirm Button Component

This component defines a button used for confirming actions. It emits a 'confirmClicked' event when clicked.

Author: ChacalTordu
-->

<template>
  <button @click="handleClick" class="myButton">{{ textButton }}</button>
</template>

<script setup>
const props = defineProps({ textButton: String });
const emit = defineEmits(['confirmClicked']);

/**
* Handles the button click event
* Emits 'confirmClicked' event when clicked
*/
const handleClick = () => {
  emit('confirmClicked');
};
</script>

<style scoped>
/**
* Button Styles
* Defines styles for the confirm button.
*/
.myButton {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 150px;
  padding: 10px 20px;
  font-size: 16px;
  background-color: var(--secondary-color-4);
  color: #ffffff;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

/**
* Button Hover Effect
* Defines hover effect for the confirm button.
*/
.myButton:hover {
  background-color: var(--black-color-2);
}
</style>
