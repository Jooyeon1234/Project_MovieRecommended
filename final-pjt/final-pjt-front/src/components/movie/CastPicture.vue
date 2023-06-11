<template>
    <div v-if="cast">
      <img :src="castURL" alt="">
    </div>
  </template>
  
  <script>
  export default {
    name: "MovieVideo",
    props:{
      cast: Object,
    },
    computed: {
      castURL(){
        const castPhoto = this.cast.profile_path
        return `https://image.tmdb.org/t/p/w600_and_h900_bestv2${castPhoto}`
      }
    }
  }
  </script>
  
  <style>
  img {
    width: 110px;
    height: 165px;
  }
  </style>