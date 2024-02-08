<template>
    <div>
        <button @click="abort" class="myButton">{{ textButton }}</button>
    </div>
</template>
  
<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({ textButton: String });
const emit = defineEmits();

const abort = () => {
    emit('abort');
};
</script>
  
<style scoped>
.myButton {
    margin-top: 10px;
    padding: 10px 20px;
    font-size: 16px;
    background-color: var(--red-color-4);
    color: #ffffff;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.myButton:hover {
    background-color:  var(--red-color-5);
}
</style>
