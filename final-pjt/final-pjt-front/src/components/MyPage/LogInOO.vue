<template>
  <div>
    <SearchBar/>
    <CurrentMovieList/>
    <UpComingMovieList/>
  </div>
</template>

<script>
import SearchBar from '../Search/SearchBar.vue';
import CurrentMovieList from '../Home/CurrentMovieList.vue';
import UpComingMovieList from '../Home/UpComingMovieList.vue';

export default {
  name : 'LoginOO',
  components:{
    SearchBar,
    CurrentMovieList,
    UpComingMovieList
  }
}
</script>

<style>

</style>