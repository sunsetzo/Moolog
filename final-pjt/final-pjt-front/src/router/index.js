import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieView from '../views/MovieView.vue'
import GameView from '../views/GameView.vue'
import ProfileEditView from '../views/ProfileEditView.vue'
import SignUpView from '../views/SignUpView.vue'


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
    path: '/profileedit',
    name: 'profileedit',
    component: ProfileEditView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
