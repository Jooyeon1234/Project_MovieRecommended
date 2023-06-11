<template>
  <li @click="selectVideo">
    <img :src="youtubeImageSrc" alt="">
    {{ video.snippet.title }}
  </li>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video:Object
  },
  methods: {
    selectVideo(){
      this.$emit('select-video', this.video)
    }
  },
  computed: {
    youtubeImageSrc(){
      return this.video.snippet.thumbnails.default.url
    }
  }
}
</script>

<style>

</style>