<template>
  <div>
    <div class="d-flex justify-content-center">
      <div class="review-box bg-dark text-white">
        <br>
        <div class="review-main">
          <div v-if="review.userpoint <= -10" class="d-flex justify-content-start ms-4">
            <h1 class="over-lines">{{ review.title }}</h1>
          </div>
          <div v-else class="d-flex justify-content-start ms-4">
            <h1>{{ review.title }}</h1>
          </div>
          <div class="d-flex justify-content-between ms-4 me-4">
            <div class="d-flex justify-content-start">
              <RouterLink 
              :to="`/profile/${review.username}`" 
              active-class="active"
              style="margin-right: 10px;">
              <p>{{ review.username }}</p>
              </RouterLink>
              <p style="margin-right: 10px;">|</p>
              <p>{{ review.created_at | formatDate }}</p> 
            </div>

            <span v-if="userCheck(review.username)">
              <!-- <button class="btn btn-link text-white text-decoration-none" data-bs-toggle="modal" data-bs-target="#updateModal">수정</button>
              <button class="btn btn-link text-white text-decoration-none" @click="deleteReview">삭제</button> -->
              <a href="#" class="text-white text-decoration-none" data-bs-toggle="modal" data-bs-target="#updateModal" style="margin-right: 10px;">수정</a>
              <a href="#" class="text-white text-decoration-none" @click="deleteReview">삭제</a>
            </span>

          </div>
        </div>
        <hr>
        <!-- <button v-if="userCheck(review.username)" class="btn btn-success" @click="updateReview">update</button> -->

        <div>
          <div class="modal fade" id="updateModal" tabindex="-1" aria-labelledby="updateModalLabel" aria-hidden="true" @hidden="hideBackdrop">
            <div class="modal-dialog">
              <div class="modal-content bg-dark text-white">
                <div class="modal-header">
                  <h1 class="modal-title fs-5" id="updateModalLabel">리뷰 생성</h1>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <form>
                    <div class="mb-3">
                      <label for="updatetitle" class="form-label">title</label>
                      <input type="text" class="form-control" id="updatetitle" v-model="updatetitle">
                    </div>
                    <div class="mb-3">
                      <label for="updatecontent" class="form-label">content</label>
                      <input type="text" class="form-control" id="updatecontent" v-model="updatecontent">
                    </div>
                    <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="updateReview">Create</button>
                  </form>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                </div>
              </div>
            </div>
          </div>
        </div>


        
        <div v-if="review.userpoint <= -10">
          <h3 class="over-lines">{{ review.content }}</h3>
        </div>
        <div v-else>
          <h3>{{ review.content }}</h3>
        </div>
        
        <div class="like-box d-flex justify-content-center">

          <span class="d-flex justify-content-center p-4 m-3">
            
            <div class="thumb">
              <button @click="likeToggle" class="btn rounded-circle" style="width: 60px; height: 60px; border-radius: 50%; background-color: #007bff;">
                <i class="fas fa-thumbs-up fa-2xl" :style="{ color: nowhobulho.like ? '#ffc107' : 'white' }"></i>
                <b>{{ review.like_review_users_count }}</b>
              </button>
            </div>

            <div class="thumb">
              <button @click="dislikeToggle" class="btn rounded-circle" style="width: 60px; height: 60px; border-radius: 50%; background-color: #dc3545;">
                <i class="fas fa-thumbs-down fa-2xl" :style="{ color: nowhobulho.dislike ? '#ffc107' : 'white' }"></i>
                <b>{{ review.dislike_review_users_count }}</b>
              </button>
            </div>

          </span>
    
        </div>
      </div>
    </div>

    <hr><br><br>

    
    <h3 class="text-white">전체 댓글 {{ review.comment_count }}개</h3>

    <form @submit.prevent="createComment(review.id)">
    <input type="text" v-model.trim="commenttext" class="commentinput">
    <button class="btn btn-light btn-sm">submit</button>
    </form>
    <br>


      <div v-for="comment in comments" :key="comment.id" class="d-flex justify-content-center">


        <div class="d-flex bg-dark border border-white text-white review-comment align-items-center" style="padding-right: 50px;">

          <div class="d-flex align-items-center ms-3" style="width: 90%; padding-right: 50px;">

            <div>
              <RouterLink 
              :to="`/profile/${comment.username}`" 
              active-class="active"
              class="d-flex justify-content-center">
                <div>
                  <img v-if="comment.userImg" :src="`http://127.0.0.1:8000/media/${comment.userImg}`" alt="no profile" style="width:80px; height: 80px;" 
                  class="rounded-circle original-image">
                  <img v-else src="../../assets/normaluser.jpg" alt="no profile" style="width:60px; height: 80px;" 
                  class="rounded-circle original-image">
                  <!-- <img :src="`http://127.0.0.1:8000/media/$`"> -->
                  <div class="d-flex justify-content-center item-align-center">
                    <div v-if="comment.username === review.username">
                      <i class="fa-regular fa-id-badge fa-lg" style="color: #ffffff; margin-right: 5px;"></i>
                    </div>
                    <!-- <p class="text-white">{{ comment.username }}</p> -->
                    <p v-if="comment.userpoint >= 10" style="color: rgb(41, 91, 255);"> {{ comment.username }}</p>
                    <p v-else-if="comment.userpoint <= -10" style="color: rgb(255, 51, 0);">{{ comment.username }}</p>
                    <p v-else style="color: white;">{{ comment.username }}</p>
                    <!-- <p v-if="comment.username === review.username" class="text-white" style="font-size: 5px;">oner</p> -->
                  </div>
                </div>
              </RouterLink>
            </div>
            
            <div v-if="comment.userpoint <= -10" class="comment-real" style="max-width: 800px; width: 80%;">
              <h4 class="ms-3 over-lines" >{{ comment.content }}</h4> 
            </div>
            <div v-else class="comment-real" style="max-width: 800px; width: 80%; word-wrap: break-word;">
              <h4 class="ms-3" style="">{{ comment.content }}</h4> 
            </div>
            
          </div>

          <div class="comment-user">
            <a href="#" v-if="userCheck(comment.username)" class=" me-5" @click="deleteComment(comment.id)">삭제</a>
            <p v-else>    </p>
          </div>
        </div>

      </div>



  </div>
</template>

<script>
import axios from 'axios'
const BASE_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewDetail',
  components: {

  },
  data(){
    return{
      review: {},
      comments: [],
      commenttext: '',
      nowhobulho: {like:false, dislike:false},
      updatetitle: '',
      updatecontent: ''
    }
  },
  created(){
    this.getReview()
  },
  filters: {
    formatDate(value) {
      const date = new Date(value);
      const year = date.getFullYear();
      const month = date.getMonth() + 1;
      const day = date.getDate();
      const hours = date.getHours();
      const minutes = date.getMinutes();

      return `${year}. ${month}. ${day} ${hours}:${minutes}`;
    },
  },
  computed:{
    
  },
  methods: {
    userCheck(nowUser) {
        return this.$store.state.username === nowUser;
      },
    isLogin(){
            return this.$store.getters.isLogin
        },
    getReview(){
      if(this.isLogin()){
        const id = this.$route.params.id
        axios({
          method: 'get',
          url: `${BASE_URL}/community/review/${id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then((res) => {
            // console.log(res.data)
            this.review = res.data
            this.getComments()
            this.nowLiked()
          })
          .catch((err) => {
            this.$router.push('/404')
            console.log(err)
            })
      } else{
        this.$router.push({name:'login'})
      }
    },
    deleteReview(){
      axios({
        method: 'delete',
        url: `${BASE_URL}/community/review/${this.review.id}`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
      })
        .then(() => {
          this.$router.push({name: 'reviews'})
        })
        .catch(err => console.log(err))
    },
    // updateReview(){
    //   this.$router.push({name:'updatereview', params: { id : this.review.id}})
    // },
    updateReview() {
            if (this.updatetitle && this.updatecontent) {
                axios({
                    method: 'put',
                    url: `${BASE_URL}/community/review/${this.review.id}/`,
                    data: { title: this.updatetitle, content: this.updatecontent },
                    headers: {
                        Authorization: `Token ${this.$store.state.token}`
                    }
                })
                    .then(() => {
                        // console.log(res)
                        this.getReview()

                    })
                    .catch(err => console.log(err))
            } else {
                alert('제목과 내용을 모두 입력해주세요')
            }
        },
    hideBackdrop() {
          const backdrop = document.querySelector('.modal-backdrop')
          if (backdrop) {
            backdrop.classList.remove('show')
          }
        },
    getComments(){
      this.comments = this.review.comment_set
      // console.log(this.comments)
    },
    createComment(id){
      if(this.commenttext){
        axios({
          method: 'post',
          url: `${BASE_URL}/community/review/${id}/comments/`,
          data: { content: this.commenttext },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
          // console.log(res.data)
          this.commenttext=''
          this.getReview()
          
        })
        .catch(err => console.log(err.response))
      } else {
        alert('할 일을 입력해주세요')
      }
    },
    deleteComment(commentId){
      axios({
        method: 'delete',
        url: `${BASE_URL}/community/comments/${commentId}`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
      })
        .then(() => {
          this.getReview()
        })
        .catch(err => console.log(err))
    },
    likeToggle(){
      axios({
        method: 'post',
        url: `${BASE_URL}/community/${this.review.id}/likes/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
      })
        .then(() => {
          // console.log(res.data)
          this.getReview()
        })
        .catch(err => console.log(err))
    },
    dislikeToggle(){
      axios({
        method: 'post',
        url: `${BASE_URL}/community/${this.review.id}/dislikes/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
      })
        .then(() => {
          this.getReview()
        })
        .catch(err => console.log(err))
    },
    nowLiked(){
      if(this.review.like_review_users.includes(this.$store.state.userid)){
        this.nowhobulho.like = true
      }else{
        this.nowhobulho.like = false
      }
      if(this.review.dislike_review_users.includes(this.$store.state.userid)){
        this.nowhobulho.dislike = true
      }else{
        this.nowhobulho.dislike = false
      }
      // console.log(this.review)
      // console.log(this.nowhobulho)
    }
  }
}
</script>

<style scoped>
.btn {
  margin-left: 5px;
}
.commentinput {
  color: black;
}

.review-comment {
  border-radius: 10px;
  width: 60%;
  min-height: 140px;
  margin-bottom: 30px;
}

.review-box {
  border: solid white;
  /* margin-left: 100px;
  margin-right: 100px; */
  width: 60%;
  border-radius: 30px;
}

.review-main {
  border-bottom: white;
}

.over-lines {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    -webkit-line-clamp: 1; /* 표시할 줄 수 */
    word-wrap: break-word;
  }
</style>