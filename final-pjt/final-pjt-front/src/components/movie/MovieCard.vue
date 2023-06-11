<template>
  <div
    @mouseover="showInfo = true; getRating()"
    @mouseleave="showInfo = false"
    @click="movieDetail(movie.id)"
    class="movie"
    :style="{ backgroundImage: `url(${movieImage})` }"
  >
    <div
      class="info bg-dark"
      :class="{ highlighted: showInfo }"
    >
      <div class="year" v-if="!showInfo"><b>{{ dateRe }}</b></div>
      <div v-if="!showInfo" class="title"><b>{{ movie.title }}</b></div>
      <div v-if="showInfo" class="h5"><b>{{ movie.title }}</b></div>
      <div class="year" v-if="showInfo"><b>{{ dateRe }}</b></div>
      <br>
      <div v-if="showInfo" class="rating">
        <span v-for="i in getStarCountfull()" :key="i" class="star filled">
            <i class="fas fa-star"></i>
        </span>
        <span v-if="roundedRating%2===1" class="star"><i class="fas fa-star"></i></span>
      </div>
      <br>
      <div v-if="showInfo" class="overview">{{ truncateOverview(movie.overview, 5) }}</div>
    </div>
  </div>
</template>


<script>
export default {
  name: "MovieCard",
  props: {
    movie: Object
  },
  data() {
    return {
      showInfo: false,
      roundedRating: 0,
    };
  },
  created(){
  },
  computed: {
    movieImage() {
      return `https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${this.movie.poster_path}`;
    },
    dateRe() {
      const dataMake = this.movie.released_date;
      const year = new Date(dataMake).getFullYear();
      return year;
    },
  },
  methods: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
    movieDetail(id) {
      if (this.isLogin()) {
        this.$router.push({ name: "moviedetail", params: { id: id } });
      } else {
        alert('로그인 해주세요!');
      }
    },
    truncateOverview(overview, maxLines) {
    //   this.roundedRating = Math.round(this.movie.vote_avg * 2) / 2;
      const lines = overview.split('\n');
      const truncatedLines = lines.slice(0, maxLines);
      return truncatedLines.join('\n') + (lines.length > maxLines ? '...' : '');
    },
    getRating(){
        this.roundedRating = Math.round(this.movie.vote_avg);
        // console.log(this.roundedRating)
    },
    getStarCountfull(){
        if(this.roundedRating >= 10){
            // this.roundedRating = 0
            return 5;
        }
        else if(this.roundedRating >= 8){
            // this.roundedRating -= 8
            return 4;
        }
        else if(this.roundedRating >= 6){
            // this.roundedRating -= 6
            return 3;
        }
        else if(this.roundedRating >= 4){
            // this.roundedRating -= 4
            return 2;
        }
        else if(this.roundedRating >= 2){
            // this.roundedRating -= 2
            return 1;
        }
        else{
            return 0;
        }
    },
  }
};
</script>


<style scoped>
.movie {
  width: 200px;
  height: 300px;
  margin: 10px;
  border-radius: 4px;
  background-size: cover;
  overflow: hidden;
  position: relative;
  cursor: pointer;
}

.info {
  width: 100%;
  height: 25%;
  padding: 14px;
  font-size: 14px;
  text-align: center;
  position: absolute;
  left: 0;
  bottom: 0;
  transition: height 0.3s;
  opacity: 0.8;
  color: white;
}

.title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.highlighted {
  background-color: #000;
  height: 100%;
}

.movie:hover {
  transform: scale(1.5);
  transition: transform 0.3s ease-in-out;
  z-index: 1;
}

.overview {
  max-height: calc(1.5em * 5);
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
}

.rating {
  display: flex;
  justify-content: center;
  align-items: center;
}

.star {
  display: inline-block;
  width: 16px;
  height: 16px;
  margin-right: 2px;
}

.star i {
  color: #ddd; /* 빈 별 색상 (회색) */
}

.star.filled i {
  color: #FFD700; /* 가득 찬 별 색상 (금색) */
}

</style>
