<template>
  <div>
    <div>
      <span>마 로그인 해주소!</span>
      <br>
      <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#exampleModal">Login</button>
    </div>
    <br>
    <v-app class="app-container">
        <CurrentMovieList/>
        <UpComingMovieList/>
    </v-app>
    <div>영화 추천??</div>
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

</style>