<template>
  <div>
    <h1>상영 예정 영화</h1>
    <MovieListItem v-for="(movie) in upcomingMovies" :key="movie.id" :movie="movie"/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import MovieListItem from '../Movie/MovieListItem.vue';

export default {
  name : 'UpComingMovieList',
  components :{
    MovieListItem
  },
  computed:{
    ...mapGetters(['upcomingMovies']),
  },
  created(){
    this.getUpComingMovie()
  },
  methods:{
    getUpComingMovie(){
      this.$store.dispatch('getUpComingMovies')
    }
  }
}
</script>

<style>

</style>