import axios from 'axios'
// import router from '@/router'
import createPersistedState from 'vuex-persistedstate'


const API_URL = 'http://127.0.0.1:8000'

const movie = {
  plugins:[
    createPersistedState()
  ],
  state: {
    currentMovies : [],
    upcomingMovies : [],
    Movies : []
  },
  getters: {
    currentMovies : state => state.currentMovie,
    upcomingMovies : state => state.upcomingMovies,
    Movies : state => state.Movies
  },
  mutations: {
    GET_CURRENT_MOVIES(state, movies){
        state.currentMovies = movies
    },
    GET_UPCOMING_MOVIES(state, movies){
        state.upcomingMovies = movies
    },
    GET_MOVIES(state, movies){
        state.Movies = movies
    }
  },
  actions: {
    getCurrentMovies(context){
        axios({
            method:'get',
            url: `${API_URL}`
        })
        .then((res)=>{
            console.log(res, context)
            context.commit('GET_CURRENT_MOVIES', res.data)
        })
        .catch((err)=>{
            console.log(err)
        })
    },
    getUpComingMovies(context){
        axios({
            method:'get',
            url:`$API_URL`
        })
        .then((res)=>{
            console.log(res)
            context.commit('GET_UPCOMING_MOVIES', res.data)
        })
        .catch((err)=>{
            console.log(err)
        })
    },
    getMovies(context){
        axios({
            menubar:'get',
            url:`${API_URL}`
        })
        .then((res)=>{
            console.log(res)
            context.commit('GET_MOVIES', res.data)
        })
        .catch((err)=>{
            console.log(err)
        })
    }
  },
  modules: {
  }
}


export default movie