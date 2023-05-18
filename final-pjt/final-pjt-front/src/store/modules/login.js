import axios from 'axios'
import router from '@/router'

const API_URL = 'http://127.0.0.1:8000'

const LogIn = {
  state: {
    token : null,
    authError : null,
    isAuthError : false,
  },
  getters: {
    isLogin(state){
      return state.token ? true:false
    },
    isAuthError: state => state.isAuthError,
    authError: state => state.authError,
  },
  mutations: {
    SAVE_TOKEN(state, token){
      state.token = token
      router.push({name:'HomeView'})
    },
    SET_AUTH_ERROR:(state, error)=>{
      state.authError = error
      state.isAuthError = true
    },
    DELETE_TOKEN(state){
      state.token=null
      router.push({name:'HomeView'})
    }
  },
  actions: {
    signUp(context, payload){
      const { username, nickname, email, password1, password2 } = payload

      axios({
        method:'post',
        url : `${API_URL}/accounts/signup/`,
        data :{
          username, nickname, email, password1, password2
        }
      })
      .then(res=>{
        console.log('signup res')
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(err=>{
        console.log(err, 'SIGNUP ERR')
      })
    },
    login(context, payload){
      const username = payload.username
      const password = payload.password

      axios({
        method:'post',
        url : `${API_URL}/accounts/login/`,
        data:{
          username, password
        }
      })
      .then((res)=>{
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err)=>{
        console.log(err, 'LOGINERR')
        context.commit('SET_AUTH_ERROR', err.response.data)
      })
    },
    logOut(context){
      axios({
        method:'post',
        url : `${API_URL}/accounts/logout/`,
        headers:{
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then(()=>{
        context.commit('DELETE_TOKEN')
      })
      .catch(err => console.log(err))
    }
  },
  modules: {
  }
}


export default LogIn