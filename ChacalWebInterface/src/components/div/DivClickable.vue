<template>
    <div class="mediaType">
      <div @click="handleClick(string_textDiv)">{{ string_textDiv }}</div>
    </div>
</template>
  
<script setup>
  import { ref } from 'vue';

  const props = defineProps({ string_textDiv: String });
  const emit = defineEmits(['divSelected']);

  const selectedOption = ref(null);
  
  function handleClick(string_textDiv) {
    selectedOption.value = true;
    emit('divSelected', string_textDiv);
  }
</script>

<style scoped>
.mediaType {
    margin-bottom: 10px;
    cursor : pointer;
    transition-duration: 0.2s;
    transition-timing-function: ease-in-out;
    transform-style: preserve-3d;
}

.mediaType:hover {
  transform: scale(1.1);
  backface-visibility: hidden;
}
</style>
  