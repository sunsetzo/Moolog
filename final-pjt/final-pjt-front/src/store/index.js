import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

import login from './modules/login.js'
import profileedit from './modules/profileedit.js'

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
      state.user.user_image = userinfo.user_image
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
        console.log(res)
        context.commit('GET_USER', res.data)
      })
      .catch((err)=>{
        console.log(err)
        console.log('gerUser err')
      })
    }
  },
  modules:{
    login,
    profileedit,
  }
})
