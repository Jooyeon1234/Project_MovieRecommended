<template>
  <div>
      <p><a href="#" data-bs-toggle="modal" data-bs-target="#reviewModal">리뷰생성</a></p>

    <div>
      <div class="modal fade" id="reviewModal" tabindex="-1" aria-labelledby="reviewModalLabel" aria-hidden="true" @hidden="hideBackdrop">
        <div class="modal-dialog">
          <div class="modal-content bg-dark text-white">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="reviewModalLabel">리뷰 생성</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <form>
                <div class="mb-3">
                  <label for="reviewtitle" class="form-label">title</label>
                  <input type="text" class="form-control" id="reviewtitle" v-model="reviewtitle">
                </div>
                <div class="mb-3">
                  <label for="reviewcontent" class="form-label">content</label>
                  <input type="text" class="form-control" id="reviewcontent" v-model="reviewcontent">
                </div>
                <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="createReview">Create</button>
              </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
            </div>
          </div>
        </div>
      </div>
    </div>




    <div class="reviews">
      <!-- <ReviewindIvidual v-for="review in reviews" :key="review.id" :review="review" class="review"/> -->
      <div v-for="review in reviews" :key="review.id" :review="review" class="review">
        <div class="my-3 d-flex justify-content-center">
          <div  class="bg-dark border border-white d-flex justify-content-center align-items-center review-box" style="min-height: 100px; border-radius: 20px;">
            <div>
            <RouterLink
            :to="`/reviews/${review.id}`"
            active-class="active">
              <div style="margin-left: 30px; margin-right: 30px;">
                <div class="mt-3">
                  <p class="over-lines" style="margin-left: 100px; margin-right: 100px;">{{review.id}}. {{ review.title }}</p>
                </div>
                <div v-if="review.userpoint <= -10" class="mb-3">
                  <p class="black-list">작성자 : {{ review.username }}</p>
                </div>
                <div v-else-if="review.userpoint >= 10" class="mb-3">
                  <p class="white-list">작성자 : {{ review.username }}</p>
                </div>
                <div v-else class="mb-3">
                  <p class="text-white">작성자 : {{ review.username }}</p>
                </div>
              </div>
            </RouterLink>
            </div>
            </div>
          </div>
      </div>
      
    </div>
  </div>
</template>

<script>
// import ReviewindIvidual from '@/components/review/ReviewIndividual'
import axios from 'axios'

export default {
    name: 'CommunityView',
    components: {
    // ReviewindIvidual,
  },
    data(){
        return{
          reviews: [],
          reviewtitle: '',
          reviewcontent: ''
        }
    },
    created(){
        this.getPosts()
    },
    methods: {
        getPosts(){
          if(this.$store.state.userid){
            axios({
                method: 'get',
                url: 'http://127.0.0.1:8000/community/review/',
                headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
            })
              .then((res) => {
                // console.log(res)
                if(res){
                  this.reviews = res.data
                } else{
                  this.reviews = []
                }
              })
              .catch(err => console.log(err))
          } else{
            alert('로그인 go')
          }
        },
        createReview() {
          const BASE_URL = 'http://127.0.0.1:8000'
          if (this.reviewtitle && this.reviewcontent) {
            axios({
              method: 'post',
              url: `${BASE_URL}/community/review/`,
              data: { title: this.reviewtitle, content: this.reviewcontent },
              headers: {
                Authorization: `Token ${this.$store.state.token}`
              }
            })
              .then((res) => {
                //   console.log(res.data)
                this.$router.push({ name: 'reviewdetail', params: { id: res.data.id } })
              })
              .catch((err) => {
                console.log(err)
              })
          } else {
            alert('제목과 내용을 모두 입력해주세요')
          }
        },
        hideBackdrop() {
          const backdrop = document.querySelector('.modal-backdrop')
          if (backdrop) {
            backdrop.classList.remove('show')
          }
        }
    }
}
</script>

<style scoped>

.review-box{
  width: 70%;
}

.over-lines {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    overflow: hidden;
    -webkit-line-clamp: 1; /* 표시할 줄 수 */
    word-wrap: break-word;
  }

.black-list{
  color: rgb(255, 51, 0)
}
.white-list{
  color: rgb(41, 91, 255);
}


@media(max-width: 800px){
  .review-box{
    width: 90%;
  }
}

</style>