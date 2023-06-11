<template>
  <div>
    <h1>UpdateMovieReView</h1>
    <hr><br><br><br>
    <form @submit.prevent="updateReview">
        <input type="text" v-model="title" class="updateinput"><br>
        <input type="text" v-model="content" class="updateinput"><br>
        <button class="btn btn-primary btn-sm">제출</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const BASE_URL = 'http://127.0.0.1:8000'

export default {
    name: 'UpdateReView',
    data() {
        return {
            title: '',
            content: '',
        }
    },
    created() {
    },
    methods: {
        updateReview() {
            if (this.title && this.content) {
                const id = this.$route.params.id
                console.log(id)
                axios({
                    method: 'put',
                    url: `${BASE_URL}/community/review/${id}/`,
                    data: { title: this.title, content: this.content },
                    headers: {
                        Authorization: `Token ${this.$store.state.token}`
                    }
                })
                    .then(() => {
                        this.$router.push({ name: 'reviewdetail', params: { id: id } })
                    })
                    .catch(err => console.log(err))
            } else {
                alert('제목과 내용을 모두 입력해주세요')
            }
        }
    }
}
</script>

<style>
 .updateinput {
    color: black;
 }
</style>
