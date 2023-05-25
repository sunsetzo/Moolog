<template>
  <div>
    <div class="container">
      <div class="content">
        <img src="@/assets/logout.jpg" alt="logout">
      </div>
      <div>
        <button class="btn login" data-bs-toggle="modal" data-bs-target="#exampleModal" style="color:whitesmoke">지금
          <img class="logo logo-login" src="@/assets/moolog_nobg.png" alt="logo">
        즐겨보세요!
        </button>
      </div>  
    </div>
    <v-app class="app-container">
        <CurrentMovieList/>
        <UpComingMovieList/>
    </v-app>
  </div>
</template>

<script>
import CurrentMovieList from '../Home/CurrentMovieList.vue';
import UpComingMovieList from '../Home/UpComingMovieList.vue';

export default {
  name : 'LoginXX',
  components:{
    CurrentMovieList,
    UpComingMovieList
  }
}
</script>

<style scoped>

.login {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 65%;
  height: 15%;
  transform: translate(-50%, -50%);
  font-size: 25px;
  text-align: center;
  /* width: 300px; */
}

.container {
  height: 450px;
  width: 75%;
  margin: 10px auto;
  position: relative;
}

.content img {
  width: 100%;
  opacity: 0.25;
  filter: blur(2px);
  vertical-align: middle;
}

.logo-login {
  position: relative;
  bottom: 6px;
}
</style>