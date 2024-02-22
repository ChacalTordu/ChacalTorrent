<!--
* Spinner Component Styles
* Defines the appearance and animation of a spinner component.

Author: ChacalTordu

-->
<template>
  <div class="spinner"></div>
</template>

<style scoped>
.spinner {
  /* Spinner div CSS */
  height: 40px;
  width: 40px;
  border-radius: 50%;
  border: 5px solid #ccc;
  border-top-color: var(--vt-c-text-light-2);
  animation: spin 2s linear infinite;
}

/**
* Spinner Animation
* Defines the keyframes for the spinner rotation animation.
*/
@keyframes spin {
  0% {
      transform: rotate(0deg);
  }
  100% {
      transform: rotate(360deg);
  }
}
</style>
