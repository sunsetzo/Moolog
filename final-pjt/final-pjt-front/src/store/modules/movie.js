import axios from 'axios'
// import router from '@/router'
import createPersistedState from 'vuex-persistedstate'
import {sampleSize} from 'lodash'


const API_URL = 'http://127.0.0.1:8000'

const movie = {
  plugins:[
    createPersistedState()
  ],
  state: {
    currentMovies : [],
    upcomingMovies : [],
    Movies : [],
    randomMovie : null,
    showRandomMovie : false,
  },
  getters: {
    currentMovies : state => state.currentMovie,
    upcomingMovies : state => state.upcomingMovies,
    Movies : state => state.Movies,
    randomMovie : state => state.randomMovie
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
    },
    getRandomMovie(state){
        state.randomMovie = sampleSize(state.Movies, 1)
        state.showRandomMovie = true
    }
  },
  actions: {
    getCurrentMovies(context){
        axios({
            method:'get',
            url: `${API_URL}/api/v1/now_playing_movies/`,
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
    },
    
  },
  modules: {
  }
}


export default movie