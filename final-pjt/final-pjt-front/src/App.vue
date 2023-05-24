<template>
  <div id="app">
    <header>
      <div class="d-flex">
        <div>
          <img class="logo" src="@/assets/moolog_nobg.png" alt="logo" data-bs-toggle="modal" data-bs-target="#randomMovieModal">
          <RandomMovie/>
        </div>
        <nav>
          <router-link class="router-link-a" :to="{name : 'home'}">Home</router-link>
          <router-link class="router-link-a" :to="{name : 'movie'}">Movie</router-link>
          <router-link class="router-link-a" :to="{name : 'game'}">Game</router-link>
        </nav>
      </div>
      <div>
        <!-- 버튼 눌렀을 때
        1) 로그인이 안되어 있으면 로그인 모달창
        2) 로그인이 되어 있으면 프로필 수정 및 로그아웃 버튼-->
        <div v-if="isLogin" class="d-flex align-items-center me-1">
          <div class="main-profile">
            <img v-if="profileImg" :src="profileImg" alt="profileImg" class="main-profile-img">
            <img v-else src="@/assets/user_img.png" alt="profileImg" class="main-profile-img">
            <p class="me-1 nickname-p">{{ nickname }}님 <i class="fa-regular fa-face-laugh-squint" style="color: #ffffff;"></i></p>
          </div>
          <div class="dropdown">
            <button class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            </button>
            <ul class="dropdown-menu">
              <li><router-link :to="{name : 'mypage' }" class="dropdown-item"> MY PROFILE</router-link></li>
              <li><router-link :to="{name : 'profileedit'}" class="dropdown-item">USER EDIT</router-link></li>
              <li><a class="dropdown-item" @click="logOut">LOGOUT</a></li>
            </ul>
          </div>
        </div>
        <div v-if="!isLogin">
          <!-- 로그인 모달 -->
          <button data-bs-toggle="modal" data-bs-target="#exampleModal" style="color:whitesmoke;" class="mt-4 me-3">Login</button>
          <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header" style="background-color: #7E57C2; color:white; height:3.5rem">
                  <v-toolbar-title class="modal-title" style="font-size:large; font-weight:bold">Login</v-toolbar-title>
                  <button type="button" class="btn btn-custom-close" data-bs-dismiss="modal" aria-label="Close" style="position: relative; left: 12px;"><i class="fa-solid fa-xmark fa-lg"></i></button>
                </div>
                <div class="modal-body">
                  <div class="mb-3">
                    <div class="d-flex ms-1">
                      <label for="username" class="form-label">ID</label>
                    </div>
                    <input type="text" class="form-control" id="username" aria-describedby="emailHelp" v-model="username">
                  </div>
                  <div class="mb-3">
                    <div class="d-flex ms-1">
                      <label for="loginPW" class="form-label">PASSWORD</label>
                    </div>
                    <input type="password" class="form-control" id="loginPW" aria-describedby="emailHelp" v-model="password" @keyup.enter="logIn">
                  </div>
                  <div class="d-flex justify-content-end">
                    <a href="#" data-bs-toggle="tooltip" title="비밀번호를 찾는 창을 띄워줍니다.">
                      <button class="btn fs-6" data-bs-target="#exampleModalToggle2" data-bs-toggle="modal" data-bs-dismiss="modal" style="background-color: white; color:#757575;">Forgot Password?</button>
                    </a>
                  </div>
                  <div class="d-flex justify-content-end">
                    <a href="#" data-bs-toggle="tooltip" title="회원 가입 페이지로 이동합니다.">
                      <button class="btn fs-6" data-bs-dismiss="modal" style="color:#7E57C2;" @click="signUp">Are you not a member yet?</button>
                    </a>
                  </div>
                </div>
                <!-- 계정 연동 로그인 -->
                <div>
                  <GoogleLogin/>
                  <NaverLogin/>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn" data-bs-dismiss="modal" @click="logIn" style="background-color: #7E57C2; color:white;">LogIn</button>
                  <!-- <button data-bs-dismiss="modal" @click="signUp">SignUp</button> -->
                </div>
              </div>
            </div>
          </div>
          <!-- 비밀번호 찾기 모달 창 -->
          <div class="modal fade" id="exampleModalToggle2" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
            <div class="modal-dialog modal-dialog-centered">
              <div class="modal-content">
                <div class="modal-header" style="background-color: #7E57C2; color:white; height:3.5rem">
                  <v-toolbar-title class="modal-title" style="font-size:large; font-weight:bold">Find Password</v-toolbar-title>
                  <button type="button" class="btn btn-custom-close" data-bs-dismiss="modal" aria-label="Close" style="position: relative; left: 12px;"><i class="fa-solid fa-xmark fa-lg"></i></button>
                </div>
                <div class="modal-body">
                  <div class="mb-3">
                    <div class="d-flex ms-1">
                      <label for="email" class="form-label">Please enter your email</label>
                    </div>
                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" v-model="email">
                  </div>
                </div>
                <div class="modal-footer">
                  <button class="btn" data-bs-dismiss="modal" @click="resetPW(email)" style="background-color: #7E57C2; color:white;">OK</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    <router-view @editProfile="getNickname"/>
  </div>
</template>

<script>
import axios from 'axios'
import GoogleLogin from './components/Social/GoogleLogin.vue'
import NaverLogin from './components/Social/NaverLogin.vue'
import RandomMovie from './components/Movie/RandomMovie.vue'
import { mapGetters } from 'vuex'

export default {
  name:'App',
  components: {
    GoogleLogin,
    NaverLogin,
    RandomMovie,
  },
  data(){
    return{
      username : null,
      password : null,
      loginuser : '',
      email : null,
      // google-login
      showRandomMovie : this.$store.state.movie.showRandomMovie,
    }
  },
  created(){
    this.getUser()

    if (this.isLogin) {
      this.loginuser = this.$store.state.user.nickname
  }
  this.getMovie()
  // this.getAllMoivie()
},
  computed : {
    ... mapGetters(['userInfo']),
    isLogin(){
      return this.$store.getters.isLogin
    },
    nickname(){
      return this.userInfo.nickname
    },
    profileImg(){
      return this.userInfo.user_image
    }
  },
  methods:{
    logIn(){
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }

      this.$store.dispatch('login', payload)

      this.username=''
      this.password=''
    },
    signUp(){
      this.$router.push('signup')
    },
    logOut(){
      this.$store.dispatch('logOut')
      this.$store.commit('LOGOUT_USER')
      // this.$router.push('home')
    },
    getNickname(nickname){
      console.log(nickname)
      // this.loginuser = nickname
    },
    findPW(){
      console.log(this.isForgot)
      this.$store.dispatch('findPW')
    },
    resetPW(email){
      this.$store.dispatch('resetPW', email)
      this.email=''
    },
    getUser(){
      this.$store.dispatch('getUser')
      // console.log(currentUser)
      // this.loginuser = this.currentUser.nickname
    },
    getMovie(){
      this.$store.dispatch('getMovies')
    },
    getAllMoivie(){
      this.$store.commit('GET_ALL_MOVIES')
    },
    // google
    onSuccess(googleUser){
      console.log(googleUser)
      axios({
        methods:'post',
        url : 'http://127.0.0.1:8000/accounts/allauth/google/login/'
        
      })
    },
    // getRandomMovie(){
    //   this.$store.commit('getRandomMovie')
    // }
  }
}
</script>

<style>
body, html {
  background-color: black;
  /* 다른 스타일 속성들 */
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: black;

  width: 100%;
  height: 100%;
}
header{
  display: flex;
  justify-content: space-between;
}

nav {
  padding-top: 18px;
  padding-left: 15px;
}

nav a {
  text-decoration-line: none;
  font-weight: 500;
  color: #ffffff;
}

nav a.router-link-exact-active {
  color: #4DD0E1;
}
li {
  list-style : none;
}
li a {
  text-decoration: none;
}
.main-profile{
  display: flex;
  margin-top: 5px;
}
.main-profile-img{
  margin: 5px;
  width: 40px;
  height: 40px;
  border-radius: 30%;
}
.logo{
  margin-top: 10px;
  margin-left: 10px;
  width: 200px;
}

.router-link-a {
  font-size: 20px;
  margin-right: 15px;
  padding: 0;
}

header {
  height: 60px;
}

.nickname-p {
  color:whitesmoke;
  margin-top: 14px;
}

.dropdown .btn {
  color: whitesmoke;
  width: auto; /* 기본값이 가로 전체를 차지하므로 auto로 설정합니다 */
  margin-top: 5px;
  padding: 0.25rem 0.25rem; /* 버튼 내부의 패딩 값을 조정하여 크기를 조절합니다 */
}

.btn-custom-close {
  color: white !important;
  font-size: 1rem;
  opacity: 1;
  transition: opacity 0.3s ease-in-out;
}

.btn-custom-close:hover {
  opacity: 0.8;
}
</style>
