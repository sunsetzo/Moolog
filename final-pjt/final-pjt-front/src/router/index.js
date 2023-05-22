import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieView from '../views/MovieView.vue'
import GameView from '../views/GameView.vue'
import MyPageView from '../views/MyPageView.vue'
import ProfileEditView from '../views/ProfileEditView.vue'
import SignUpView from '../views/SignUpView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import CurrentMovieDetail from '../views/CurrentMovieDetail'
import UpComingMovieDetail from '../views/UpComingMovieDetail'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/game',
    name: 'game',
    component: GameView
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: MyPageView
  },
  {
    path: '/profileedit',
    name: 'profileedit',
    component: ProfileEditView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/movie/detail/:id',
    name: 'moviedetail',
    component: MovieDetailView,
  },
  {
    path: '/movie/detail/:id',
    name: 'currentmovie',
    component: CurrentMovieDetail
  },
  {
    path: '/movie/detail/:id',
    name: 'upcomingmovie',
    component: UpComingMovieDetail
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
