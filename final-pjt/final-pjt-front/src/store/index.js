import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

import login from './modules/login.js'
import profileedit from './modules/profileedit.js'
import password from './modules/password.js'
import follow from './modules/follow.js'
import movie from './modules/movie.js'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[createPersistedState()],
  state: {
    user : [],
  },
  getters: {
  },
  mutations: {
    GET_USER(state, user){
      state.user = user
      console.log(state.user)
    },
    SAVE_NEW_PROFILE(state, userinfo){
      console.log(userinfo)
      state.user.nickname = userinfo.nickname
      // state.user.user_image = userinfo.user_image
      alert('수정되었습니다!')
      router.push({name:'home'})
    },
    SAVE_NEW_IMAGE(state, userinfo){
      state.user.user_image = userinfo.user_image
    },
    SAVE_PW(state, userpw){
      console.log(userpw)
      state.user.password = userpw
    },
    LOGOUT_USER(state){
      state.user = []
    }
  },
  actions: {
    getUser(context){
      axios({
        method:'get',
        url:`${API_URL}/accounts/user/`,
        headers :{
          Authorization:`Token ${ context.rootState.login.token }`
        }
      })
      .then((res) => {
        console.log('getUser success')
        // console.log(res)
        // console.log(res.data.user_image)
        context.commit('GET_USER', res.data)
      })
      .catch((err)=>{
        console.log(err)
        console.log('getUser err')
      })
    }
  },
  modules:{
    login,
    profileedit,
    password,
    follow,
    movie,
  }
})
