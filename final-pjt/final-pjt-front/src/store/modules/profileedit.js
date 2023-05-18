import axios from 'axios'
// import router from '@/router'
import createPersistedState from 'vuex-persistedstate'


const API_URL = 'http://127.0.0.1:8000'

const profileEdit = {
  plugins:[
    createPersistedState()
  ],
  state: {
  },
  getters: {
  },
  mutations: {
    // SAVE_NEW_PROFILE(state, userinfo){
    //   console.log(state)
    //   console.log(userinfo)
    // }
  },
  actions: {
    editProfile(context, params){
      const { nickname, user_image, token } = params
      console.log(token)
      console.log(nickname)
      console.log(user_image)
      axios({
        method:'put',
        url : `${API_URL}/accounts/user/`,
        data:{
          nickname,
          user_image
        },
        headers:{
          Authorization: `Token ${ token }`
        }
      })
      .then((res)=>{
        console.log(res)
        context.commit('SAVE_NEW_PROFILE', res)
      })
      .catch((err)=>{
        console.log(err)
        console.log('edit profile err')
      })
    }
  },
  modules: {
  }
}


export default profileEdit