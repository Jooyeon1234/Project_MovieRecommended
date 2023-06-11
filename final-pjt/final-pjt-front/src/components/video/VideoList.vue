<template>
  <div>
    <ul>
      <VideoListItem v-for="(video, idx) in videos.slice(1)"     :key="idx" 
      :video="video"
      @select-video="onSelectVideo"
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'
export default {
  name: 'VideoList',
  props: {
    videos: Array,
  },
  components: {
    VideoListItem
  },
  methods: {
    onSelectVideo(video){
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>