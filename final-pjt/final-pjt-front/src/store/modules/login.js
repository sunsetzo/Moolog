import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'


const API_URL = 'http://127.0.0.1:8000'

const LogIn = {
  plugins:[
    createPersistedState()
  ],
  state: {
    token : null,
    authError : null,
    isAuthError : false,
    userInfo : null,
  },
  getters: {
    isLogin(state){
      return state.token ? true:false
    },
    currentUser : state => state.userInfo,
    isAuthError: state => state.isAuthError,
    authError: state => state.authError,
  },
  mutations: {
    SIGN_UP_SAVE_TOKEN(state, token){
      state.token = token
      // router.push({name:'home'})
    },
    SAVE_TOKEN(state, token){
      state.token = token
      router.go(router.currentRoute)
    },
    SET_AUTH_ERROR:(state, error)=>{
      state.authError = error
      state.isAuthError = true
    },
    DELETE_TOKEN(state){
      state.token = null
      alert('로그아웃 되었습니다')
      if (this.$route.path!=='/'){
        router.push({name:'home'})
      }
      // router.go(router.currentRoute)
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
        context.commit('SIGN_UP_SAVE_TOKEN', res.data.key)
        router.push({name:'home'})
      })
      .catch(err=>{
        console.log(err.response.data, 'SIGNUP ERR')
        const errorMessages = Object.values(err.response.data)[0];
        console.log(errorMessages)
        alert(errorMessages)
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
        console.log(err, 'LOGIN ERR')
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
    },
    signOut(context, userinfo){
      console.log(userinfo)
      console.log(context)
      axios({
        method:'post',
        url: `${API_URL}/accounts/signout/`,
        headers:{
          Authorization: `Token ${ context.state.token }`
        }
      })
      .then((res)=>{
        console.log(res, 'signout success')
        context.commit('DELETE_TOKEN')
      })
      .catch((err)=>{
        console.log(err, 'signout fail')
      })
    }
  },
  modules: {
  }
}


export default LogIn