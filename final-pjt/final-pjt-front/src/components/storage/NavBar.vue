<template>
  <div>
    <header class="d-flex align-items-center" style="margin-bottom: 50px;">
      <Logo style="width: 45%;"/>

      <div class="nav mx-5 d-flex" style="width: 30%;">
        <div v-if="isLogin" class="d-flex" style="margin-right: 100px;">
          <span v-for="nav in islognav" :key="nav.name" class="nav-item">
            <RouterLink :to="nav.href" active-class="active" class="nav-link">
              <button type="button" class="btn btn-outline-light">{{ nav.name }}</button>
            </RouterLink>
          </span>
        </div>

        <div v-else class="d-flex" style="margin-right: 100px;">
          <div
            v-for="nav in nolognav" :key="nav.name" class="nav-item">
            <RouterLink :to="nav.href" active-class="active" class="nav-link">
              <button type="button" class="btn btn-outline-light">{{ nav.name }}</button>
            </RouterLink>
          </div>
        </div>
      </div>



      <div>
        
        <div class="d-flex justify-content-end">
          <div v-if="this.$store.state.userid" class="profile-container">
            <div v-if="user.userImg" class="d-flex text-white">
              <img :src="profileUrl" alt="no profile" style="width:60px; height:60px;" class="rounded-circle original-image" @click="toggleItems">
              <p>{{ user.username }}</p>
            </div>
            <div v-else class="d-flex text-white">
              <img src="../../assets/normaluser.jpg" alt="no profile" style="width:60px; height:60px;" class="rounded-circle original-image" @click="toggleItems">
              <p>{{ user.username }}</p>
            </div>
            <transition name="slide-down">
              <div v-if="showItems" class="slide-down-content" style="width: 100px; max-height: 200px; background-color: black">
                <RouterLink :to="'/logout'" active-class="active"><p>로그아웃</p></RouterLink><hr>
                <RouterLink :to="`/profile/${myname}`" active-class="active"><p>{{ user.username }}</p></RouterLink>
              </div>
            </transition>
          </div>

          <div v-else class="profile-container">
            <img src="../../assets/normaluser.jpg" alt="no img" style="width: 60px; height: 60px;" class="rounded-circle original-image" @click="toggleItems">
            <transition name="slide-down">
              <div v-if="showItems" class="slide-down-content" style="width: 100px; max-height: 200px; background-color: black">
                <!-- <RouterLink :to="'/login'" active-class="active"><p>로그인</p></RouterLink> -->
                <!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">로그인</button>
                <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#signupModal">회원가입</button> -->
                <p><a href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">로그인</a></p>
                <p><a href="#" data-bs-toggle="modal" data-bs-target="#signupModal">회원가입</a></p>
                <!-- <RouterLink :to="'/signup'" active-class="active"><p>회원가입</p></RouterLink> -->
              </div>
            </transition>
          </div>
        </div>


        <div>
          <!-- 로그인 모달 -->
          <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content bg-dark text-white">
                <div class="modal-header">
                  <h1 class="modal-title fs-5" id="exampleModalLabel">로그인</h1>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <!-- 로그인 폼 -->
                  <form @submit.prevent="login">
                    <div class="mb-3">
                      <label for="username" class="form-label">사용자명</label>
                      <input type="text" class="form-control" id="username" v-model="username">
                    </div>
                    <div class="mb-3">
                      <label for="password" class="form-label">비밀번호</label>
                      <input type="password" class="form-control" id="password" v-model="password">
                    </div>
                    <button type="button" class="btn btn-primary" @click="login">로그인</button>
                  </form>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                </div>
              </div>
            </div>
          </div>

          <!-- 회원가입 모달 -->
          <div class="modal fade" id="signupModal" tabindex="-1" aria-labelledby="signupModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content bg-dark text-white">
                <div class="modal-header">
                  <h1 class="modal-title fs-5" id="signupModalLabel">회원가입</h1>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <!-- 회원가입 폼 -->
                  <form>
                    <div class="mb-3">
                      <label for="createusername" class="form-label">사용자명</label>
                      <input type="text" class="form-control" id="createusername" v-model="createusername">
                    </div>
                    <div class="mb-3">
                      <label for="createpassword1" class="form-label">비밀번호</label>
                      <input type="password" class="form-control" id="createpassword1" v-model="createpassword1">
                    </div>
                    <div class="mb-3">
                      <label for="createpassword2" class="form-label">비밀번호 확인</label>
                      <input type="password" class="form-control" id="createpassword2" v-model="createpassword2">
                    </div>
                    <button type="button" class="btn btn-primary" @click="signup">회원가입</button>
                  </form>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                </div>
              </div>
            </div>
          </div>
      </div>




      </div>

    </header>
  </div>
</template>

<script>
import Logo from '@/components/storage/LoGo'
import axios from 'axios'
// import router from '@/router'
const BASE_URL = 'http://127.0.0.1:8000'


export default {
  components: {
    Logo
  },
  data() {
    return {
      islognav: [
        {
        name: 'Search',
        href: '/',
        },
        {
          name: 'Reviews',
          href: '/reviews',
        },
      ],
      nolognav: [
        {
        name: 'Search',
        href: '/',
        },
      ],
      showItems: false, 
      user : {},
      username: '', // 이메일 입력값
      password: '', // 비밀번호 입력값
      createusername: '',       // 회원가입 사용자명 입력값
      createpassword1: '',      // 회원가입 비밀번호 입력값
      createpassword2: '',      // 회원가입 비밀번호 확인 입력값
    }
  },
  created(){
    this.getProfile()
  },
  computed: {
    isLogin(){
      return this.$store.getters.isLogin
        },
    myname(){
      return this.$store.state.username
    },
    profileUrl(){
          return `http://127.0.0.1:8000${this.user.userImg}`
        }
  },
  methods: {
    getProfile(){
      if(this.isLogin){
        axios({
          method: 'get',
          url: `${BASE_URL}/accounts/profile/${this.$store.state.username}/`
        })
          .then((res) => {
            // console.log(res.data)
            this.user = res.data
          })
          .catch(err => console.log(err))
      }
    },
    toggleItems(){
      this.showItems = !this.showItems
      // console.log(this.showItems)
    },
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    login() {
      if(!this.username){
        alert('아이디를 입력해주세요')
      } else if(!this.password) {
        alert('비밀번호를 입력해주세요')
      } else{
        const username = this.username
        const password = this.password
  
        const payload = {
          username,
          password
        }
        this.$store.dispatch('logIn', payload)
      }
    },
    signup() {
      if(!this.createusername){
        alert('아이디를 입력해주세요')
      } else if(!this.createpassword1){
        alert('비밀번호1을 입력해주세요')
      } else if(!this.createpassword2){
        alert('비밀번호2를 입력해주세요')
      } else if(this.createpassword1 != this.createpassword2){
        alert('비밀번호가 일치하지 않습니다.')
      }
      else{
        const username = this.createusername
        const password1 = this.createpassword1
        const password2 = this.createpassword2
  
        const payload = {
          username,
          password1,
          password2
        }
        this.$store.dispatch('signUp', payload)
      }
      


    }
    
  },
  
}
</script>

<style>
header {
    height: 100
    px;
    align-content: center;
    border-bottom: solid 1px white;
}
header .nav {
    font-size: 20px;
}
.profile-container {
  position: relative;
  display: inline-block;
}

.slide-down-content {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  padding: 10px;
  z-index: 100;
}

.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.3s ease;
}

.slide-down-enter,
.slide-down-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

a{text-decoration:none; color: white}

.modal {
  display: none;
  background-color: rgba(0, 0, 0, 0.5);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1050;
}

.modal.show {
  display: block;
}


</style>