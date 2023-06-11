<template>
  <RouterLink 
    to="/home" 
    class="logo">
    <span class="tmdblogo"> <span class="tmdb">TMTV</span>.COM</span>
  </RouterLink>
</template>

<style>
.logo {
  font-family: "Oswald", sans-serif;
  font-size: 40px;
  color: black;
  text-decoration: none;
  /* &:hover {
    color: $black;
  } */
}
.tmdb {
color: rgb(0, 0, 255);
}
.tmdblogo {
  font-size: 50px;
}
</style>