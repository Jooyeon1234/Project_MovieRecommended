<template>
  <div class="text-white">
    <br>
    <!-- <h1>profile view</h1> -->
    
    <div class=" d-flex justify-content-around m-5">
      
      <div @mouseover="changeColor(true)"
        @mouseleave="changeColor(false)"
        @click="uploadImage"
        class="image-container mt-3"
      >
        <img v-if="!myId.userImg" src="../../assets/normaluser.jpg" alt="" style="width:400px; height:400px;"  class="rounded-circle original-image">
        <img v-else :src="profileUrl" alt="no profile" style="width:400px; height:400px;" 
        class="rounded-circle original-image border border-3">
        <i class="fa-regular fa-image fa-6x hover-image" ></i>
        <input type="file" ref="fileInput" @change="onFileChange"  style="display:none;">
      </div>

      <div class="d-flex flex-column mt-4" style="margin-right : 400px;">
        
        <h1 v-if="myId.userpoint >= 10" style="color: rgb(41, 91, 255);">{{myname}}님</h1>
        <h1 v-else-if="myId.userpoint <= -10" style="color: rgb(255, 51, 0);">{{myname}}님</h1>
        <h1 v-else style="color: white;">{{myname}}님</h1>

        <div v-if="!userCheck(myId.username)">

          
          <button  v-if="!isLiked" @click="followToggle" class="btn btn-primary mt-5 btn-lg">
            <i class="fa-regular fa-user fa-beat fa-xs"></i> follow</button>
          <button  v-else @click="followToggle" class="btn btn-danger mt-5 btn-lg">
            <i class="fa-solid fa-user-slash fa-beat fa-xs"></i> follow 취소</button>
        </div>
        
        <br><br>
        <h2>팔로워 : {{ myId.followers_count }}</h2>
        <br>
        <h2>팔로잉 : {{ myId.followings_count }}</h2>
        <br>
        <h2>포인트 : {{ myId.point }}</h2>
      
      </div>
      
    </div>
    

    <br><br><hr>


    
    <div class="d-flex justify-content-center">
      <div class="profile-content-box" style="width: 80%; min-height: 700px;">

        <!-- // 프로필 항목 분할 -->
        <div class="d-flex profile-content-button" style="width: 100%;">
          <span v-for="page in profilePage" :key="page" style="width: 25%;">
            <button @click="pageChange(page)" class="pageButton btn btn-outline-light" :class="nowPage === page ? 'btn-selected' : 'btn-unselected'" style="width: 100%; height: 50px;">{{ page }}</button>
          </span>
        </div>

        <!-- // 좋아하는 영화 -->
        <div v-if="nowPage === 'MyMovie'">
          <h2 class="mt-5">{{ myname }}님이 좋아하는 영화</h2>
          <br>
          <div class="carousel-container">
            <div class="carousel-block" style="width: 900px">
              <Carousel id="home-carousel" 
              :per-page="3"
              :autoplay="true"
              :loop="true"
              :autoplay-timeout="3000"
              >
                <Slide v-for="movie in myMovies" :key="movie.id">
                  <RouterLink :to="`/movies/${movie.id}`" active-class="active">
                  <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${movie.poster_path}`" style="width: 300px; height: 450px;">
                  </RouterLink>
                </Slide>
              </Carousel>
            </div>
          </div>
        </div>

        <!-- // 영화 코멘트 -->
        <div v-if="nowPage === 'MovieComment'">
          <h2 class="mt-5">{{myname}}님이 영화에 작성한 코멘트</h2>
          <div class="my-3 d-flex justify-content-center" v-for="comment in myMovieComment" :key="comment.commentId">
            <div class="my-movie-comment bg-dark border border-white my-2 d-flex align-items-center" style="min-height: 100px; width: 80%;">
              
              <div style="width: 20%;" class="d-flex justify-content-center">
                
                <RouterLink 
                    :to="`/profile/${comment.username}`" 
                    active-class="active"
                    class="nav-link d-flex justify-content-center ms-5">
                      <div>
                        <img v-if="!myId.userImg" src="../../assets/normaluser.jpg" style="width:80px; height: 80px;" 
                        class="rounded-circle original-image">
                        <img v-else :src="`http://127.0.0.1:8000/media/${comment.userImg}`" alt="no profile" style="width:80px; height: 80px;" 
                        class="rounded-circle original-image">
                        <h5 class="text-white">{{ comment.username }}</h5>
                      </div>
                </RouterLink>
                
              </div>
              
              <div style="width: 60%;">
                <RouterLink 
                    :to="`/movies/${comment.movie.id}`" 
                    active-class="active"
                    class="d-flex justify-content-around"
                    >
                    <div>
                      <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${comment.movie.poster_path}`">
                    </div>

                    <div class="col align-self-center">
                      <div class="d-flex-col">
                        
                        <div>
                          {{ comment.movie.title}}
                        </div>

                        <div>
                          {{ comment.content }}
                        </div>

                        <div>
                          {{ comment.vote_detail }}점
                        </div>

                      </div>
                    </div>

                </RouterLink>
              </div>
              
             

              <div style="width: 20%;">{{ comment.created_at | formatDate }}</div>
              
            </div>
          </div>
        </div>
        
        <!-- // 작성리뷰 -->
        <div v-if="nowPage === 'MyReview'">
          <h2 class="mt-5">{{myname}}님이 작성한 글</h2>
          <div class="my-3 d-flex justify-content-center" v-for="post in myPosts" :key="post.id">
            <div class="my-movie-comment bg-dark border border-white my-2 d-flex align-items-center" style="min-height: 100px; width: 80%;">
              
              <div style="width: 20%;">
                
                <RouterLink 
                  :to="`/profile/${post.username}`" 
                  active-class="active"
                  class="nav-link d-flex justify-content-center ms-5">
                    <div>
                      <img v-if="!myId.userImg" src="../../assets/normaluser.jpg" style="width:80px; height: 80px;" 
                        class="rounded-circle original-image">
                      <img v-else :src="`http://127.0.0.1:8000/media/${post.userImg}`" alt="no profile" style="width:80px; height: 80px;" 
                      class="rounded-circle original-image">
                      <h5 class="text-white">{{ post.username }}</h5>
                    </div>
                </RouterLink>
              </div>
              
              <div style="width: 60%;">
                
                  <RouterLink 
                      :to="`/reviews/${post.id}`" 
                      active-class="active"
                      >
                      <h4>{{ post.title }}</h4>
                  </RouterLink>
                
              </div>

              <div style="width: 20%;">{{ post.created_at | formatDate }}</div>

            </div>
          </div>
        </div>
        
        <!-- // 리뷰코멘트 -->
        <div v-if="nowPage === 'ReviewComment'">
          <h2 class="mt-5">{{myname}}님이 리뷰에 작성한 코멘트</h2>
          <div class="my-3 d-flex justify-content-center" v-for="comment in myReviewComment" :key="comment.reviewId">
            <div 
              class="my-movie-comment bg-dark border border-white my-2 d-flex align-items-center" 
              style="min-height: 100px; width: 80%;"
            >
              
              <div style="width: 20%;">
                <RouterLink 
                  :to="`/profile/${comment.username}`" 
                  active-class="active"
                  class="nav-link d-flex justify-content-center ms-5">
                    <div>
                      <img v-if="!myId.userImg" src="../../assets/normaluser.jpg" style="width:80px; height: 80px;" 
                        class="rounded-circle original-image">
                      <img v-else :src="`http://127.0.0.1:8000/media/${comment.userImg}`" alt="no profile" style="width:80px; height: 80px;" 
                      class="rounded-circle original-image">
                      <h5 class="text-white">{{ comment.username }}</h5>
                    </div>
                </RouterLink>

              </div>
              
              <div style="width: 60%;">
                <RouterLink 
                    :to="`/reviews/${comment.review}`" 
                    active-class="active"
                    >
                    <h4 style="word-wrap: break-word;">{{ comment.content }}</h4>
                </RouterLink>

              </div>
              
              <div style="width: 20%;">{{ comment.created_at | formatDate }}</div>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import { Carousel, Slide } from "vue-carousel"
import router from '@/router'


const BASE_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ProfileView',
    components:{
      Carousel,
      Slide,

    },
    data(){
        return {
            myId: {},
            movies: [],
            reviews: [],
            moviecomments: [],
            reviewcomments: [],
            carouselOptions: {
              items: 3,
            },
            profilePage: [
              'MyMovie', 'MovieComment', 'MyReview', 'ReviewComment'
            ],
            nowPage: 'MyMovie',
            file: null,
            isLiked: null,
            isHovered : false,
        }
    },
    created(){
        this.getMovies()
        this.getPosts()
        this.getMovieComment()
        this.getReviewComment()
        this.getId()
        
    },
    filters: {
      formatDate(value) {
        const date = new Date(value);
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();
        // const hours = date.getHours();
        // const minutes = date.getMinutes();

        return `${year}. ${month}. ${day}`;
      },
    },
    computed: {
        myname(){
          return this.$route.params.username
        },
        myMovies() {
          return this.movies.filter(movie => {
            if (movie.like_users) {
              return movie.like_users.some(user => user === this.myId.id);
            }
            return false;
          });
        },
        myPosts(){
            return this.reviews.filter(review =>
            review.username === this.myname
            )
        },
        myMovieComment(){
            return this.moviecomments.filter(comment =>
            comment.username === this.myname
            )
        },
        myReviewComment(){
            return this.reviewcomments.filter(comment =>
            comment.username === this.myname
            )
        },
        profileUrl(){
          return `http://127.0.0.1:8000${this.myId.userImg}`
        }
    },
    methods: {
      pageChange(now){
        this.nowPage = now
      },
        uploadImage() {
          if(this.userCheck(this.myId.username)){
            this.$refs.fileInput.click();

          }
        },
        
        onFileChange(e) {
          // console.log(e.target.files[0])
          this.file = e.target.files[0];
          this.uploadFile()
        },
        uploadFile() {
          let formData = new FormData();
          const token =  this.$store.state.token
          const headers = {Authorization: `Token ${token}`}
          formData.append("userImg", this.file);
          axios.post(`${BASE_URL}/accounts/profile/${this.myname}/`, formData , {headers}).then((res) => {
            console.log("File uploaded successfully");
            console.log(res);
            this.getId()
            router.go(router.currentRoute)
          }).catch(err => console.log(err))
        },


        userCheck(nowUser) {
          return this.$store.state.username === nowUser;
        },
        getMovies(){
            axios({
                method: 'get',
                url: `${BASE_URL}/movies/home/`,
                headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
            })
              .then((res) => {
                // console.log(res.data)
                this.movies = res.data
              })
              .catch(err => console.log(err))
        },
        getPosts(){
            axios({
                method: 'get',
                url: `${BASE_URL}/community/review/`,
                headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
            })
              .then((res) => {
                // console.log(res.data)
                this.reviews = res.data
              })
              .catch(err => console.log(err))
        },
        getMovieComment(){
            axios({
                method: 'get',
                url: `${BASE_URL}/movies/comments/`,
                headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
            })
              .then((res) => {
                // console.log(res.data)
                this.moviecomments = res.data
              })
              .catch(err => console.log(err))
        },
        getReviewComment(){
            axios({
                method: 'get',
                url: `${BASE_URL}/community/review/comments/`,
                headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
            })
              .then((res) => {
                // console.log(res.data)
                this.reviewcomments = res.data
              })
              .catch(err => console.log(err))
        },
        getId(){
          axios({
            method: 'get',
            url: `${BASE_URL}/accounts/profile/${this.myname}/`,

          })
            .then((res) => {
              // console.log(res.data)
              this.myId = res.data
              this.nowFollowed()
              
            })
            .catch((err) => {
              this.$router.push('/404')
              console.log(err)
            })
          },
        followToggle(){
          axios({
            method: 'post',
            url: `${BASE_URL}/accounts/${this.myId.id}/follow/`,
            headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
          })
            .then((res) => {
              console.log(res.data)
              this.isLiked = res.data.is_followed
              this.getId()
            })
            .catch(err => console.log(err))
        },
        nowFollowed(){
          if(this.myId.followers.includes(this.$store.state.userid)){
            this.isLiked = true
          }else{
            this.isLiked = false
          }
        },
        changeColor(isHovered){
          this.isHovered = isHovered
        }
      },
      beforeRouteUpdate(to, from, next){
        this.getId.username = to.params.username
        next()
        router.go(router.currentRoute)
      },
    }
</script>

<style scoped>
.carousel-container {
  display: flex;
  justify-content: center;
}

.carousel-block {
  width: 900px;
}

.image-container {
  position: relative;
  margin-left: 200px;
}

.original-image {
  /* filter: brightness(70%); */
  transition: filter 0.5s ease;
  transition: transform 0.5s ease;
}

.hover-image {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  opacity: 0;
  
}

.image-container:hover .hover-image {
  opacity: 1;
}

.image-container:hover .original-image {
  filter: brightness(70%) ;
  transform: scale(1.1);
  
}

.profile-content-box{
  /* border: solid 1px rgb(22, 22, 22); */
  border-radius: 20px;
  /* background-color: rgb(22, 22, 22); */
}

.pageButton{
  border-radius: 10px;
  
}

.btn-selected{
  /* border-bottom: solid 3px white; */
  /* background-color: black; */
}
.btn-unselected{
  /* background-color: black; */
}

.my-movie-comment{
  /* background-color: rgb(22, 22, 22); */
  border-radius: 15px;
}

</style>