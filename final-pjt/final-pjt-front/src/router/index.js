import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieView from '../views/MovieView.vue'
import GameView from '../views/GameView.vue'
import MyPageView from '../views/MyPageView.vue'
import ProfileEditView from '../views/ProfileEditView.vue'
import SignUpView from '../views/SignUpView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import CurrentMovieDetail from '../views/CurrentMovieDetail.vue'
import UpComingMovieDetail from '../views/UpComingMovieDetail.vue'
import UserPageView from '../views/UserPageView.vue'
import FindCardGame from '../views/FindCardGame.vue'

import SearchResult from '../components/Search/SearchResult.vue'
import SearchResultRe from '../components/Search/SearchResultRe.vue'

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
    path: '/findcardgame',
    name: 'findcardgame',
    component: FindCardGame
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: MyPageView
  },
  {
    path: '/userprofile/:userid',
    name: 'userprofile',
    component: UserPageView
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
  {
    path: '/movie/search/',
    name: 'search',
    component: SearchResult,
    props: (route) => ({ SearchResult: route.query.SearchResult })
  },
  {
    path: '/movie/search_re/',
    name: 'search_re',
    component: SearchResultRe,
    props: (route) => ({ SearchResult: route.query.SearchResult })
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
