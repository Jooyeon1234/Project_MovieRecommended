<template>
  <div id="app">
    <NavBar />

    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/storage/NavBar'

export default {
  components : {
    NavBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* background-color: black; */
  /* background-color: black; */
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

body {
  background-color: black;
}
</style>
