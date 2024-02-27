<template>
    <div class="mediaType">
      <div @click="handleClick(textDiv)">{{ textDiv }}</div>
    </div>
</template>
  
<script setup>
  import { ref, defineProps, defineEmits } from 'vue';

  const props = defineProps({ textDiv: String });
  const emit = defineEmits(['divSelected']);

  const selectedOption = ref(null);
  
  function handleClick(textDiv) {
    selectedOption.value = true;
    emit('divSelected', textDiv);
  }
</script>

<style scoped>
.mediaType {
    cursor : pointer; 
}
</style>
  