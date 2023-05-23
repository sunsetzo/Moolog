import axios from 'axios'
// import router from '@/router'
import createPersistedState from 'vuex-persistedstate'


const API_URL = 'http://127.0.0.1:8000'

const userprofile = {
  plugins:[
    createPersistedState()
  ],
  state: {
    userprofile : []
  },
  getters: {
    userprofile : state => state.userprofile
  },
  mutations: {
    GET_USER_PROFILE(state, res){
      state.userprofile = res
    }
  },
  actions: {
    getUserProfile(context){
      axios({
        method:'get',
        url : `${API_URL}/accounts/profile/:user_id`
      })
      .then((res)=>{
        console.log(res, 'user profile res')
        context.commit('GET_USER_PROFILE')
      })
      .catch((err)=>{
        console.log(err, 'user profile err')
      })
    }
  },
  modules: {
  }
}


export default userprofile