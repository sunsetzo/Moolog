import axios from 'axios'
// import router from '@/router'
import createPersistedState from 'vuex-persistedstate'


const API_URL = 'http://127.0.0.1:8000'

const passwordEdit = {
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
    completePW(context, payloadPW){
      const { oldpassword, password, token } = payloadPW
      axios({
        method:'post',
        url : `${API_URL}/accounts/password/change/`,
        data : {
          old_password : oldpassword,
          new_password1 : password,
          new_password2 : password,
        },
        headers:{
          Authorization: `Token ${ token }`,
        }
      })
      .then((res)=>{
        console.log(res, 'success pw')
        context.commit('SAVE_PW', res)
      })
      .catch((err)=>{
        console.log(err, 'fail pw')
        alert('기존 비밀번호가 일치하지 않습니다.')
      })
    },
    resetPW(context, email){
      axios({
        method:'post',
        url : `${API_URL}/accounts/password/reset/`,
        data : {email},
      })
      .then((res)=>{
        console.log(res)
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
  modules: {
  }
}


export default passwordEdit