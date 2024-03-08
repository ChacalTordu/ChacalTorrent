<!--
ButtonAbort.vue - Abort Button Component

This component defines a button used for aborting operations. It emits an 'abort' event when clicked.

Author: ChacalTordu

-->

<template>
    <div>
        <button @click="abort" class="myButton">{{ textButton }}</button>
    </div>
</template>
  
<script setup>
const props = defineProps({ textButton: String });
const emit = defineEmits();

/**
 * Aborts the operation
 * Emits 'abort' event when clicked
 */
const abort = () => {
    emit('abort');
};
</script>
  
<style scoped>
/**
 * Button Styles
 * Defines styles for the abort button.
 */
.myButton {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 150px;
    max-width: 70px;
    padding: 10px 20px;
    font-size: 16px;
    background-color: var(--accent-color-red);
    color: #ffffff;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

/**
 * Button Hover Effect
 * Defines hover effect for the abort button.
 */
.myButton:hover {
    background-color:  var(--black-color-2);
}
</style>
