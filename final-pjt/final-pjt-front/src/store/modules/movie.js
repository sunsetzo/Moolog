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
    currentMovies : state => state.currentMovies,
    upcomingMovies : state => state.upcomingMovies,
    Movies : state => state.Movies,
    randomMovie : state => state.randomMovie,
    allMovies : state => state.allMovies
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
    },
    // GET_ALL_MOVIES(state){
    //     state.currentMovies.forEach((el)=>{
    //         state.allMovies.push(el)
    //     })
    //     state.upcomingMovies.forEach((el)=>{
    //         state.allMovies.push(el)
    //     })
    //     state.Movies.forEach((el)=>{
    //         state.allMovies.push(el)
    //     })
    // }
  },
  actions: {
    getCurrentMovies(context){
        axios({
            method:'get',
            url: `${API_URL}/api/v1/now_playing_movies/`,
        })
        .then((res)=>{
            // console.log(res, context)
            context.commit('GET_CURRENT_MOVIES', res.data)
        })
        .catch((err)=>{
            console.log(err)
        })
    },
    getUpComingMovies(context){
        axios({
            method:'get',
            url:`${API_URL}/api/v1/upcoming_movies/`
        })
        .then((res)=>{
            // console.log(res)
            context.commit('GET_UPCOMING_MOVIES', res.data)
        })
        .catch((err)=>{
            console.log(err)
        })
    },
    getMovies(context){
        axios({
            method:'get',
            url:`${API_URL}/api/v1/popular_movies/`
        })
        .then((res)=>{
            // console.log(res)
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