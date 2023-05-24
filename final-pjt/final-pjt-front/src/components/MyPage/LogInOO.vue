<template>
  <div>
    <SearchBar/>
    <RecommendMovie/>
    <CurrentMovieList/>
    <UpComingMovieList/>
  </div>
</template>

<script>
import SearchBar from '../Search/SearchBar.vue';
import RecommendMovie from '../Home/RecommendMovie.vue';
import CurrentMovieList from '../Home/CurrentMovieList.vue';
import UpComingMovieList from '../Home/UpComingMovieList.vue';

export default {
  name : 'LoginOO',
  components:{
    SearchBar,
    RecommendMovie,
    CurrentMovieList,
    UpComingMovieList
  },
}
</script>

<style scoped>

</style>