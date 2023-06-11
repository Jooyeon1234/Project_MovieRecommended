<template>
  <div></div>
</template>

<script>
export default {
    name: 'LogOut',
    created(){
        this.logOut()
    },
    methods:{
        logOut(){
            this.$store.dispatch('logOut')
        }
    },
}
</script>

<style>

</style>