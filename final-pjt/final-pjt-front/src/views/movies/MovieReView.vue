<template>
    <div>
      <h1>CreateReView</h1>
      <hr><br><br><br>
      <form @submit.prevent="createReview">
          <input type="text" v-model="title" class="createinput"><br>
          <input type="text" v-model="content" class="createinput"><br>
          <button class="btn btn-primary btn-sm">제출</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
      name: 'CreateReView',
      data() {
          return {
              title: '',
              content: '',
          }
      },
      methods: {
      createReview(){
        const BASE_URL = 'http://127.0.0.1:8000'
        if(this.title && this.content){
          axios({
            method: 'post',
            url: `${BASE_URL}/community/review/`,
            data: { title: this.title, content:this.content },
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
          .then((res) => {
          //   console.log(res.data)
          this.$router.push({name:'reviewdetail' , params:{id:res.data.id}})
          })
          .catch(err => console.log(err.response))
        } else {
          alert('할 일을 입력해주세요')
        }
      }
      }
  }
  </script>
  
  <style>
   .createinput {
      color: black;
   }
  </style>