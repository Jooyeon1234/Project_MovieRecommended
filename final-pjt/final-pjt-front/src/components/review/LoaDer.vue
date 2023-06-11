<template>
  <carousel
    :responsive="{0:{items:3,nav:false,dots:false},600:{items:5,nav:false,dots:true}}"
  >
    <img v-for="(img, index) in images" :src="img" :key="index">
  </carousel>
</template>

<script>
import carousel from "vue-owl-carousel";

export default {
  components: {
    carousel
  },
  name: "HelloWorld",
  data: function() {
    return {
      images: [
        "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg",
        "https://www.themoviedb.org/movie/385687-fast-x?language=ko",
        "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg",
        "https://www.themoviedb.org/movie/385687-fast-x?language=ko",
        "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg",
        "https://www.themoviedb.org/movie/385687-fast-x?language=ko",
        "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/dlGyzCxbBQK1U2O5o31Z1hB6erc.jpg",
        "https://www.themoviedb.org/movie/385687-fast-x?language=ko",

      ]
    };
  },
};