<template>
  <div id="app">
    <header>
      <div>
        <img src="" alt="logo">
      </div>
      <nav>
        <router-link :to="{name : 'home'}">Home</router-link> |
        <router-link :to="{name : 'movie'}">Movie</router-link> |
        <router-link :to="{name : 'game'}">Game</router-link> |
      </nav>
      <div>
        <!-- 버튼 눌렀을 때
        1) 로그인이 안되어 있으면 로그인 모달창
        2) 로그인이 되어 있으면 프로필 수정 및 로그아웃 버튼-->
        <div class="dropdown">
          <button data-bs-toggle="modal" data-bs-target="#exampleModal">임시 프로필 이미지 버튼</button>
          <div v-if="isLogin">
            <ul class="dropdwon-menu">
              <li><router-link :to="{name : 'profileedit'}">ProfileEdit</router-link></li>
              <li @click="logOut">Logout</li>
            </ul>
          </div>
          <div v-else>
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
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="logIn">LogIn</button>
                    <button data-bs-dismiss="modal" @click="signUp">SignUp</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
    <router-view/>
  </div>
</template>

<script>
export default {
  name:'App',
  data(){
    return{
      username : null,
      password : null,
      showModal : true,
    }
  },
  computed : {
    isLogin(){
      return this.$store.getters.isLogin
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
    },
    signUp(){
      this.$router.push('signup')
    },
    logOut(){
      this.$store.dispatch('logOut')
      this.$router.push('HomeView')
    }
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
