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
  },
  actions: {
    uploadImg(context, payload){
      const {image, token} = payload
      console.log(image)
      console.log(token)
      const formData = new FormData()
      formData.append('user_image', image)
      console.log(formData)
      axios({
        method:'put',
        url : `${API_URL}/accounts/user/`,
        data: formData,
        headers:{
          Authorization: `Token ${ token }`,
          'Content-Type': 'multipart/form-data'
        }
      })
      .then((res)=>{
        console.log(res, 'uploadimg success')
        context.commit('SAVE_NEW_IMAGE', res)
      })
      .catch((err)=>{
        console.log(err, 'uploadImg fail')
      })

    },
    editProfile(context, params){
      const { nickname, token } = params
      axios({
        method:'put',
        url : `${API_URL}/accounts/user/`,
        data: {nickname},
        headers:{
          Authorization: `Token ${ token }`,
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