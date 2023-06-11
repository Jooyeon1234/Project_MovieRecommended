<template>
  <div class="container">
    <h1>Sign Up Page</h1>
    <div>
      <form @submit.prevent="signup">
        <label for="username">username</label><br>
        <input type="text" id="username" v-model="username" class="input-field"><br><br>

        <label for="password1">password1</label><br>
        <input type="password" id="password1" v-model="password1" class="input-field"><br><br>

        <label for="password2">password2</label><br>
        <input type="password" id="password2" v-model="password2" class="input-field"><br><br>

        <input type="submit" value="SignUp" class="btn btn-primary wide-btn">
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signup() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username,
        password1,
        password2
      }
      this.$store.dispatch('signUp', payload)
    }
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
