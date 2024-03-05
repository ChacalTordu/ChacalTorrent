<!--
Sucess.vue - SVG Animation Component

This component defines SVG animations for displaying different shapes and styles.
It includes animations for circles and polylines, as well as text styles.

Author: ChacalTordu

-->

<template>
  <div>
    <svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 130.2 130.2">
      <circle class="path circle" fill="none" stroke="#0D5B1B" stroke-width="6" stroke-miterlimit="10" cx="65.1" cy="65.1" r="62.1"/>
      <polyline class="path check" fill="none" stroke="#0D5B1B" stroke-width="6" stroke-linecap="round" stroke-miterlimit="10" points="100.2,40.2 51.5,88.8 29.8,67.5 "/>
    </svg>
  </div>
</template>

<style scoped>
/**
 * SVG Animation Styles
 * Defines the animation for SVG elements such as circles and polylines.
 */

svg {
  width: 40px;
  display: block;
}

/**
 * Path Animation
 * Defines the animation for stroke-dasharray and stroke-dashoffset for SVG paths.
 */
.path {
  stroke-dasharray: 1000;
  stroke-dashoffset: 0;
  &.circle {
    -webkit-animation: dash .9s ease-in-out;
    animation: dash .9s ease-in-out;
  }
  &.check {
    stroke-dashoffset: -100;
    -webkit-animation: dash-check 8s .35s ease-in-out forwards;
    animation: dash-check 3s .35s ease-in-out forwards;
  }
}

/**
 * Text Style
 * Defines the style for text elements within the template.
 */
p {
  text-align: center;
  margin: 20px 0 60px;
  font-size: 1.25em;
  &.success {
    color: var(--green2-color-5);
  }
}

/**
 * Keyframes for Path Animation
 * Defines the keyframes for path animations.
 */
@-webkit-keyframes dash {
  0% {
    stroke-dashoffset: 1000;
  }
  100% {
    stroke-dashoffset: 0;
  }
}

@keyframes dash {
  0% {
    stroke-dashoffset: 1000;
  }
  100% {
    stroke-dashoffset: 0;
  }
}

/**
 * Keyframes for Check Animation
 * Defines the keyframes for check animation.
 */
@-webkit-keyframes dash-check {
  0% {
    stroke-dashoffset: -100;
  }
  100% {
    stroke-dashoffset: 900;
  }
}

@keyframes dash-check {
  0% {
    stroke-dashoffset: -100;
  }
  100% {
    stroke-dashoffset: 900;
  }
}
</style>
