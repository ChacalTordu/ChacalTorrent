<template>
    <button @click="handleClick" class="myButton">{{ textButton }}</button>
</template>
  
<script setup>
   const props = defineProps({textButton : String});
   const emits = defineEmits(['confirmClicked']);

   const handleClick = () => {
    emits('confirmClicked')
  };
</script>
  
<style scoped>
  .myButton {
    width: 150px;
    padding: 10px 20px;
    font-size: 16px;
    background-color: var(--green2-color-4);
    color: #ffffff;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .myButton:hover {
    background-color: var(--green2-color-5);
  }
</style>
  