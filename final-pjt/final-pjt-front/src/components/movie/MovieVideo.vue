<template>
    <div v-if="video" style="width: 100%; height: 100%;">
      <iframe :src="videoURL" frameborder="0" style="width: 100%; height: 100%;"></iframe>
    </div>
  </template>
  
  <script>
  export default {
    name: "MovieVideo",
    props:{
      video: Object,
    },
    computed: {
      videoURL(){
        const videoId = this.video.id.videoId
        return `https://www.youtube.com/embed/${videoId}`
      }
    }
  }
  </script>
  
  <style>
  
  </style>