<template>
  <img :src="movieData.Poster" alt="Affiche">
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';

const movieData = ref('');

const config = require('@/../../config/config.json');
const apiKey = config.apiKey_tmdb;

async function searchMovie(movieTitle) {
    try {
        const response = await axios.get(`http://www.omdbapi.com/?apikey=${apiKey}&t=${movieTitle}`);
        movieData.value = response.data;
    } catch (error) {
        console.error('Erreur lors de la recherche du film :', error);
    }
};
</script>
