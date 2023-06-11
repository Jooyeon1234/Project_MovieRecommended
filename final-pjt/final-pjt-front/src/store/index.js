import router from '@/router'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
// import { get } from 'core-js/core/dict'
import Vue from 'vue'
import Vuex from 'vuex'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    token: null,
    username: null,
    userid: null
  },
  getters: {
    isLogin(state){
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_TOKEN(state, token){
      state.token = token
      // router.push({name: 'home'})
    },
    DELETE_TOKEN(state){
      state.token = null
      router.push({name: 'home'})
    },
    SET_USERNAME(state, username) {
      state.username = username;
    },
    SET_USERID(state, userid) {
      state.userid = userid;
    }

  },
  actions: {
    signUp(context, payload){
      const {username, password1, password2} = payload
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          // console.log(res)
          // this.state.username = username
          context.commit('SAVE_TOKEN', res.data.key)
          // router.push({ name: 'login' })
          axios({
            method: 'get',
            url: `${API_URL}/accounts/profile/${username}/`
          })
            .then((profileRes) => {
              context.commit('SET_USERNAME', username);
              context.commit('SET_USERID', profileRes.data.id);
              router.go(router.currentRoute)
            })
            .catch((err) => {
              console.log(err)
              alert('다시 입력해 주세요')
            })
          
          
        })
        .catch(err => console.log(err))
    },
    logIn(context, payload) {
      const { username, password } = payload;
        
      axios.all([
        axios.post(`${API_URL}/accounts/login/`, {
          username,
          password
        }),
        axios.get(`${API_URL}/accounts/profile/${username}/`)
      ])
        .then(axios.spread((loginRes, profileRes) => {
          // 로그인 요청 응답 처리
          context.commit('SAVE_TOKEN', loginRes.data.key);
        
          // 프로필 요청 응답 처리
          context.commit('SET_USERNAME', username);
          context.commit('SET_USERID', profileRes.data.id);
          router.go(router.currentRoute)
          // console.log(profileRes.data.id);
          
        }))
        .catch((err) => {
          console.log(err)
          alert('다시 입력해 주세요')
        })
    },
    logOut(context){
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`
      })
      .then(() => {
        // console.log(res)
        this.state.username = null
        this.state.userid = null
        context.commit('DELETE_TOKEN')
      })
      .catch(err => console.log(err))
    }
  },
  modules: {
  }
})
