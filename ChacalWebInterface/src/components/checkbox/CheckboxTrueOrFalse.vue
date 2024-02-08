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

  const props = defineProps({textCheckbox : String});
  const emits = defineEmits(['checkboxSet'])
  const checkbox1 = ref(false);
  const checkbox2 = ref(false);
  
  const handleCheckboxChange = (checkbox) => {
    emits('checkboxSet');
    if (checkbox === 'checkbox1' && checkbox1.value) {
      checkbox2.value = false;
      emits('checkboxSet',"Yes");
    } else if (checkbox === 'checkbox2' && checkbox2.value) {
      checkbox1.value = false;
      emits('checkboxSet',"No");
    }
  };
</script>

<style scoped>
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
