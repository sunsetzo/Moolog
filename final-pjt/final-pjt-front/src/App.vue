<template>
  <div id="app">
    <header>
      <div>
        <img src="" alt="logo">
      </div>
      <nav>
        <router-link :to="{name : 'home'}">Home</router-link> |
        <router-link :to="{name : 'movie'}">Movie</router-link> |
        <router-link :to="{name : 'game'}">Game</router-link>
      </nav>
      <div>
        <!-- 버튼 눌렀을 때
        1) 로그인이 안되어 있으면 로그인 모달창
        2) 로그인이 되어 있으면 프로필 수정 및 로그아웃 버튼-->
        <div v-show="isLogin" >
          <p>반갑슈 {{ loginuser }}</p>
          <div class="dropdown">
            <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
              임시 프로필 이미지
            </button>
            <ul class="dropdown-menu">
              <li><router-link :to="{name : 'mypage'}">My Page</router-link></li>
              <li><router-link :to="{name : 'profileedit'}">ProfileEdit</router-link></li>
              <li><a class="dropdown-item" @click="logOut">Logout</a></li>
            </ul>
          </div>
        </div>
          <div v-show="!isLogin">
            <button data-bs-toggle="modal" data-bs-target="#exampleModal">임시 프로필 이미지 버튼</button>
            <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Login</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <label for="username"> ID : </label>
                    <input type="text" id="username" v-model="username">
                    <br>
                    <label for="loginPW">PW : </label>
                    <input type="password" id="password" v-model="password">
                    <br>
                    <button class="btn btn-primary" data-bs-target="#exampleModalToggle2" data-bs-toggle="modal" data-bs-dismiss="modal">Forgot Password?</button>
                    
                  </div>
                  <!-- 계정 연동 로그인 -->
                  <!-- <div>
                    <div @click="GoogleLogin">구글 연동</div>
                  </div> -->
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="logIn">LogIn</button>
                    <button data-bs-dismiss="modal" @click="signUp">SignUp</button>
                  </div>
                </div>
              </div>
            </div>
            <!-- 비밀번호 찾기 모달 창 -->
            <div class="modal fade" id="exampleModalToggle2" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalToggleLabel2">비밀번호 찾기</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>이메일을 입력해주세요</p>
                    <input type="email" v-model="email">
                  </div>
                  <div class="modal-footer">
                    <button class="btn btn-primary" data-bs-dismiss="modal" @click="resetPW(email)">완료</button>
                    <button class="btn btn-primary" data-bs-dismiss="modal">닫기</button>
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
export default {
  name:'App',
  data(){
    return{
      username : null,
      password : null,
      loginuser : '',
      email : null,
    }
  },
  created(){
    this.getUser()
    if (this.isLogin) {
      this.loginuser = this.$store.state.user.nickname
  }
},
  computed : {
    isLogin(){
      return this.$store.getters.isLogin
    },
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
      this.loginuser = nickname
    },
    findPW(){
      console.log(this.isForgot)
      this.$store.dispatch('findPW')
    },
    resetPW(email){
      this.$store.dispatch('resetPW', email)
      email=''
    },
    getUser(){
      this.$store.dispatch('getUser')
    },
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
header{
  display: flex;
  justify-content: space-between;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
li{
  list-style : none;
}
</style>
