<template>
    <div class="container">
        <div :class="['movieda', {'d-flex': shouldDisplayFlex}]">
            

          <div class="poster first-content">
            <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${movie.poster_path}`">
          </div>


          <div class="movieinfo second-content">
            <div class="title">{{ movie.title }}</div>
            
            <div class="minfo">
                <span>전문가 평점 : {{ movie.vote_avg }}</span>
                <span>개봉일 : {{ movie.released_date }}</span>
            </div>
            
            <div>
            <button @click="toggleLike" class="btn heartbtn">
              <i :class="{'fas': isLiked, 'far': !isLiked, 'fa-heart': true, 'fa-fade': !isLiked}" style="color: #ff4242;"></i>
            </button>
            <span class="text-white">{{movie.like_users_count}}명이 이 영화를 좋아합니다.</span>
            </div>

            <h3>Genres</h3>
            <div class="d-flex justify-content-center">
              <div v-for="genre in movie.genres" :key="genre.id" class="genres">
                <div style="margin-right: 7px;">{{ genre.name }}</div>
                </div><br>
            </div>

            <h3>Overview</h3>
            <div class="overview">{{ movie.overview }}</div>
            
            <h3>Cast</h3>
            <div class="d-flex justify-content-center">
              <div v-for="cast in credits" :key="cast.id">
                <CastPicture :cast="cast" class="cast-picture"/>
                <p class="cast-name">{{ cast.name }}</p>  
              </div>
            </div>
          </div>
          
        </div>


        <div :class="['movietc mb-5', {'d-flex': shouldDisplayFlex}]">

          <div class="third-content movie-comment">
            <div class="comment-title d-flex justify-content-center align-items-center">
              <div class="d-flex justify-content-center align-items-center" style="width: 80%;">
                <div><h3 class="commenttitle">{{ movie.moviecomment_count }}개의 댓글 - </h3></div>
                <div class="rating">
                  <span v-for="i in getStarCountfull()" :key="i" class="star filled">
                      <i class="fas fa-star"></i>
                  </span>
                  <span v-if="roundedRating%2===1" class="star"><i class="fas fa-star"></i></span>
                </div>

              </div>
              <div v-if="!commentCheck"><button class="create-button" data-bs-toggle="modal" data-bs-target="#evalModal">create</button></div>

              <div class="modal fade" id="evalModal" tabindex="-1" aria-labelledby="evalModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                  <div class="modal-content bg-dark text-white">
                    <div class="modal-header">
                      <h1 class="modal-title fs-5" id="evalModalLabel">댓글 생성</h1>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                      <form @submit.prevent="login">
                        <div class="mb-3">
                          <label for="movieEva" class="form-label">댓글</label>
                          <input type="text" class="form-control" id="movieEva" v-model="movieEva">
                        </div>
                        <div class="mb-3">
                          <label for="movieRating" class="form-label">별점</label>
                          <input type="number" class="form-control" id="movieRating"  min="1" max="10" v-model="movieRating">
                        </div>
                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="createEvaluation">Create</button>
                      </form>
                    </div>
                    <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                    </div>
                  </div>
                </div>
              </div>



            </div>

            
            <div v-for="comment in movie.moviecomment_set" :key="comment.id">
              <div class="d-flex align-items-center comment-all">
                <div class="d-flex justify-content-center" style="width: 20%;">
                  <img v-if="comment.userImg" :src="profileUrl(comment.userImg)" alt="no profile" style="width:40px; height:40px;" class="rounded-circle original-image">
                  <img v-else src="../../assets/normaluser.jpg" alt="no profile" style="width:40px; height:40px;" class="rounded-circle original-image">
                  <RouterLink 
                    :to="`/profile/${comment.username}`" 
                    active-class="active">
                    <h4 v-if="comment.userpoint >= 10" style="color: rgb(41, 91, 255);"> {{ comment.username }}</h4>
                    <h4 v-else-if="comment.userpoint <= -10" style="color: rgb(255, 51, 0);">{{ comment.username }}</h4>
                    <h4 v-else>{{ comment.username }}</h4>
                  </RouterLink>
                </div>
                


                <div class="text-white d-flex justify-content-start" style="width: 70%;">
                  <h4 v-if="comment.userpoint <= -10" style="width: 70%; word-wrap: break-word;" class="clamp-lines">{{ comment.content }}</h4>
                  <h4 v-else style="width: 70%; word-wrap: break-word;">{{ comment.content }}</h4>


                    
                  <div class="rating mb-3" style="margin-left: 5px;">
                    <span v-for="i in getDetailCountfull(comment.vote_detail)" :key="i" class="detail-star filled">
                        <i class="fas fa-star"></i>
                    </span>
                    <span v-if="comment.vote_detail%2===1" class="detail-star"><i class="fas fa-star"></i></span>
                  </div>
                </div>

                
                <div v-if="userCheck(comment.username)">
                  <a href="#" class="text-decoration-none delete-button" style="" @click="deleteEva(comment.id)"> <h4>삭제</h4></a>
                </div>
              </div>
            </div>


          </div>

          <div class="forth-content movie-video">
            <MovieVideo :video="selectedVideo"/>
          </div>

        </div>

    </div>
  </template>
  
  <script>
import axios from 'axios'
import MovieVideo from '@/components/movie/MovieVideo'
import CastPicture from '@/components/movie/CastPicture'
const API_KEY = 'AIzaSyCL0cZvByXiANWOzaSGASR2TaE0TmvQttU'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const BASE_URL = 'http://127.0.0.1:8000'

  export default {
    name: 'MovieDetail',
    components: {
      MovieVideo,
      CastPicture
    },
    data(){
      return{
        shouldDisplayFlex: true,
        movie: {},
        videos: [],
        selectedVideo: null,
        credits: [],
        movieEva: '',
        movieRating: 0,
        ratingFilter: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        roundedRating: 0,
      }
    },
    mounted() {
      this.checkScreenSize();
      window.addEventListener('resize', this.checkScreenSize);
    },
    destroyed() {
      window.removeEventListener('resize', this.checkScreenSize);
    },
    created(){
          this.getMovie()
    },
    computed: {
      isLiked() {
        if (this.movie.like_users) {
          return this.movie.like_users.some((user) => user === this.$store.state.userid);
        }
        return false;
      },
      commentCheck() {
        if (!this.movie.moviecomment_set) {
          return false;
        }
        return this.movie.moviecomment_set.some((comment) => comment.username === this.$store.state.username);
      },
    },
    methods: {
      profileUrl(imgurl){
          return `http://127.0.0.1:8000/media/${imgurl}`
        },
      checkScreenSize() {
        this.shouldDisplayFlex = window.innerWidth > 700;
      },
      userCheck(nowUser) {
        return this.$store.state.username === nowUser;
      },
      isLogin(){
            return this.$store.getters.isLogin
        },
      getMovie(){
        if(this.isLogin()){
          const id = this.$route.params.id
          // console.log(id)
          axios({
              method: 'get',
              url: `${BASE_URL}/movies/${id}/`,
          })
            .then((res) => {
              // console.log(res.data)
              this.movie = res.data
              this.getVideo()
              this.getCredits()
              this.getRating()
            })
            .catch((err) => {
              this.$router.push('/404')
              console.log(err)
              })
        } else{alert('login go')}
              },
      getVideo(){
        const params = {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: `${this.movie.original_title} Trailer`
          }

        axios({
          method: 'get',
          url: API_URL,
          params,
      })
        .then((res) => {
          this.videos = res.data.items
          this.selectedVideo = this.videos[0]
        })
        .catch(err => console.log(err))
        },
      onSelectVideo(video){
        this.selectedVideo = video
      },
        
      getCredits(){
        const options = {
          method: 'GET',
          headers: {
            accept: 'application/json',
            Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNjY4OTgxYjhjNTFjOWRjYzhjNDkzYjg4MjRlMTEzMSIsInN1YiI6IjY0NDc2MTE1MzU4MThmMDRiY2Y4ZTMxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xjkHuY_tOAG2SGpd0AvheZ9CMTjX-YpTWKkZ1gDbYTE'
            }
        };

        fetch(`https://api.themoviedb.org/3/movie/${this.movie.id}/credits?language=ko-KR`, options)
          .then(res => res.json())
          .then((res) => {
            this.credits = res.cast.slice(0, 4)
            // console.log(this.credits)
          })
          .catch(err => console.error(err));
      },
      createEvaluation() {
        if(this.movieRating > 10){
          alert('평점은 최대 10점입니다.')
        }else{
          axios({
            method: 'post',
            url: `${BASE_URL}/movies/${this.movie.id}/comments/`,
            data: {
              content: this.movieEva,
              vote_detail: this.movieRating,
            },
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
            .then((res) => {
              console.log(res)
              this.movieEva = ''
              this.movieRating = 0
              this.getMovie()
            })
            .catch((err) => console.log(err));
        }
      },
      toggleLike(){
        axios({
          method: 'post',
          url: `${BASE_URL}/movies/${this.movie.id}/likes/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then(() => {
            // console.log(res.data)
            this.getMovie()
          })
          .catch(err => console.log(err))
      },
      deleteEva(commentId){
        axios({
          method: 'delete',
          url: `${BASE_URL}/movies/movie_comments/${commentId}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then(() => {
            this.getMovie()
          })
          .catch(err => console.log(err))
      },
      getRating(){
        this.roundedRating = Math.round(this.movie.average_vote_detail);
        // console.log(this.roundedRating)
      },
      getStarCountfull(){
        if(this.roundedRating >= 10){
            return 5;
        }
        else if(this.roundedRating >= 8){
            return 4;
        }
        else if(this.roundedRating >= 6){
            return 3;
        }
        else if(this.roundedRating >= 4){
            return 2;
        }
        else if(this.roundedRating >= 2){
            return 1;
        }
        else{
            return 0;
        }
       },
       getDetailRating(score){
        return Math.round(score)
       },
       getDetailCountfull(star){
        if(this.getDetailRating(star) >= 10){
          return 5;
        }
        else if(this.getDetailRating(star) >= 8){
            return 4;
        }
        else if(this.getDetailRating(star) >= 6){
            return 3;
        }
        else if(this.getDetailRating(star) >= 4){
            return 2;
        }
        else if(this.getDetailRating(star) >= 2){
            return 1;
        }
        else{
            return 0;
        }
       }
    }
  }
  </script>
  <style scoped>
.container {
  max-width: 1500px;
  border: solid white;
}

.movieda {
  color: gray;
  width: 100%;
  margin-top: 50px;
  display: flex; /* 추가 */
}

.poster {
  width: 50%;
  position: relative;
  margin-left: 50px;
  margin-bottom: 50px;

}

.poster img {
  width: 100%;
  height: 100%;
  border-radius: 20px;
}

.movieinfo {
  flex-grow: 1;
  width: 50%;
  margin-left: 50px;
}

.d-flex.justify-content-center {
  flex-wrap: wrap; /* 추가 */
}

.d-flex.justify-content-center > div {
  margin-bottom: 10px; /* 추가 */
}

.movieinfo .title {
  color: white;
  font-family: "Oswald", sans-serif;
  font-size: 50px;
  line-height: 1;
  margin-top: 0px;
  margin-bottom: 30px;
  font-weight: 900;
  white-space: pre-wrap;
}

.overview{
  white-space: pre-wrap;
}

  .movieinfo .minfo {
    margin-bottom: 10px;
  }
  .movieinfo .minfo span {
    margin: 0 6px;
    font-size: 20px;
  }

  h3 {
    color: white;
    margin: 12px 0 6px;
    font-family: "Oswald", sans-serif;
    font-size: 40px;
    font-weight: 1000;
  }

  .cast-name {
    color: white;
    margin-top: 0;
    text-align: center;
  }

  .star {
    cursor: pointer;
  }

  .checked {
    color: gold;
  }

  .d-flex {
    display: flex;
  }

  .align-items-center {
    align-items: center;
  }

  .justify-content-center {
    justify-content: center;
  }

  .form-group {
    margin-top: 10px;
  }

  .stars {
    display: flex;
    align-items: center;
  }

  .rating {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .star {
    display: inline-block;
    width: 30px;
    height: 30px;
    margin-right: 10px;
    font-size: 30px;
  }

  .detail-star {
    display: inline-block;
    width: 20px;
    height: 20px;
    margin-right: 5px;
    font-size: 20px;
  }

  .detail-star i {
    color: #ddd; /* 빈 별 색상 (회색) */
  }

  .detail-star.filled i {
    color: #FFD700; /* 가득 찬 별 색상 (금색) */
  }


  .star i {
    color: #ddd; /* 빈 별 색상 (회색) */
  }

  .star.filled i {
    color: #FFD700; /* 가득 찬 별 색상 (금색) */
  }

  .heartbtn {
    display: inline-block;
    padding: 5px;
    border: none;
    background-color: transparent;
    cursor: pointer;
    font-size: 50px;
  }

    .btn i {
    color: hotpink;

  }

  .movie-comment{
    width: 50%;
    margin-left: 50px;
    border: solid white;
    border-radius: 10px;
  }

  .movie-video {
  flex-grow: 1;
  width: 50%;
  max-height: 400px;
  margin-left: 50px;
  aspect-ratio: 1.5/1;
}
.movie-video MovieVideo{
  width: 100%;
  height: 100%;
}


.comment-title{
  border-bottom: solid 1px white;
}
.comment-all{
  margin-top: 7px;
  margin-bottom: 7px;
  
}
.clamp-lines {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    -webkit-line-clamp: 1; /* 표시할 줄 수 */
  }

.movietc{
  width: 100%;
}

.create-button{
  width: 100px;
  font-size: 16px;
  font-weight: 600;
  color: #fff;
  cursor: pointer;
  height: 45px;
  text-align:center;
  border: none;
  background-size: 300% 100%;

  border-radius: 50px;
  background-image: linear-gradient(to right, #29323c, #485563, #2b5876, #4e4376);
  box-shadow: 0 4px 15px 0 rgba(45, 54, 65, 0.75);
}

.create-button:hover {
    background-position: 100% 0;
    moz-transition: all .4s ease-in-out;
    -o-transition: all .4s ease-in-out;
    -webkit-transition: all .4s ease-in-out;
    transition: all .4s ease-in-out;
}

.create-button:focus {
    outline: none;
}

@media (max-width: 800px) {
  .movieda,
  .movietc {
    display: block;
  }
  
  .poster,
  .movieinfo,
  .movie-comment,
  .movie-video {
    width: 100%;
    margin-left: 5px;
  }
  .movie-comment,
  .movieinfo{
    margin-bottom: 30px;
  }

  .star {
    display: inline-block;
    width: 20px;
    height: 20px;
    margin-right: 5px;
    font-size: 20px;
  }
  .detail-star{
    display: inline-block;
    width: 10px;
    height: 10px;
    margin-right: 5px;
    font-size: 10px;
  }
  .commenttitle{
    font-size: 20px;
  }
  
}
  </style>