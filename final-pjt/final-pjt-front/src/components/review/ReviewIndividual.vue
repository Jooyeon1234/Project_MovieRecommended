<template>
  <div @click="reviewDetail(review.id)" class="review">
    <p>{{ review.title }} - {{ review.username }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: "ReviewIndividual",
  props: {
    review: Object
  },
  methods: {
    isLogin(){
            return this.$store.getters.isLogin
        },
    reviewDetail(id){
      if(this.isLogin()){
        this.$router.push({name:'reviewdetail', params: {id:id}})
      } else{
        this.$router.push({name:'login'})
      }
    }
  }
}
</script>

<style>

</style>