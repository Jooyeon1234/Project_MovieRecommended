<template>
  <div>
    <Headline style="width: 80%;"/><br><br>

    <h2 class="m-3">함께 좋아하는 영화</h2>
    <div class="carousel-contain">
      <div class="carousel-bl">
        <Carousel id="home-carousel" 
        :per-page="5"
        :autoplay="true"
        :loop="true"
        :autoplay-timeout="3000"
        >
          <Slide v-for="movie in movies" :key="movie.id">
            <RouterLink :to="`/movies/${movie.id}`" active-class="active">
            <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${movie.poster_path}`" class="recommend-movie1">
            </RouterLink>
          </Slide>
        </Carousel>
      </div>
    </div>

    <br><br>

    <h2 class="m-3">비슷한 줄거리의 영화</h2>
    <div class="carousel-contain">
      <div class="carousel-bl">
        <Carousel id="home-carousel" 
        :per-page="5"
        :autoplay="true"
        :loop="true"
        :autoplay-timeout="3000"
        >
          <Slide v-for="movie in movies2" :key="movie.id">
            <RouterLink :to="`/movies/${movie.id}`" active-class="active">
            <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${movie.poster_path}`" class="recommend-movie1">
            </RouterLink>
          </Slide>
        </Carousel>
      </div>
    </div>
  </div>

</template>

<script>
import axios from 'axios'
import Headline from '@/components/storage/HeadLine'
import { Carousel, Slide } from "vue-carousel"
const BASE_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MovieHomeView',
    components:{
        Headline,
        Carousel,
        Slide,
    },
    data(){
      return{
        movies: {},
        movies2: {},

      }
    },
    created(){
      this.getRecommendMovies()
      this.getRecommendMovies2()
    },
    computed:{
      isLogin() {
      return this.$store.getters.isLogin;
    },
    },
    methods: {
      getRecommendMovies(){
        if(this.isLogin){
          axios({
            method:'get',
            url: `${BASE_URL}/movies/recommended/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
            .then((res)=>{
              // console.log(res.data)
              this.movies = res.data.movies
            })
        }else{
          console.log('추천 영화가 없습니다.')
        }
      },
      getRecommendMovies2(){
        if(this.isLogin){
          axios({
            method:'get',
            url: `${BASE_URL}/movies/recommended2/`,
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
            .then((res)=>{
              // console.log(res.data)
              this.movies2 = res.data
            })
        }else{
          console.log('추천 영화가 없습니다.')
        }
      },
    }
}
</script>

<style scoped>
* {
    color: white;
}

.recommend-movie1{
  width: 100%;
  height: 100%;
  aspect-ratio: 1/1.5;
}
.carousel-contain {
  display: flex;
  justify-content: center;
}
.carousel-bl {
  width: 80%;
}

</style>