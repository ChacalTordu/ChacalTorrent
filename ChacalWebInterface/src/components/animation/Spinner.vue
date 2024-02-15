<template>
    <div class="spinner"></div>
</template>
<style scoped>
.spinner{
/*   spinner div css */
  height : 40px;
  width : 40px;
  border-radius : 50%;

/*   background-color : red; */
  border : 5px solid #ccc;
  border-top-color :var(--vt-c-text-light-2);
  animation : spin 2s linear infinite;
}

@keyframes spin{
  0%{
    transform : rotate(0deg);
  }
  100%{
    transform : rotate(360deg);
  }
}
</style>