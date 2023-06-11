<template>
  <div class="container">
    <h1>Log In Page</h1>
    <form @submit.prevent="login">
      <label for="username">username</label><br>
      <input type="text" id="username" v-model="username" class="input-field"><br><br>

      <label for="password">password</label><br>
      <input type="password" id="password" v-model="password" class="input-field"><br><br>
      <RouterLink to="/signup" active-class="active">
        <p>signup</p>
      </RouterLink>
      <input type="submit" value="LogIn" class="btn btn-primary wide-btn">
    </form>
  </div>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
  name: 'LoginView',
  components: {
    RouterLink,
  },
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username,
        password
      }
      this.$store.dispatch('logIn', payload)
    },
  }
}
</script>

<style scoped>
.container {
  border: solid white;
  padding: 20px;
  background-color: rgba(0, 0, 0, 0.2);
}

.input-field {
  width: 300px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  color: black;
}

.wide-btn {
  width: 300px;
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>



