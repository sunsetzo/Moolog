<template>
  <div>
    <h1>현재 상영 영화</h1>
      <MovieListItem v-for="movie in currentMovies" :key="movie.id" :movie="movie"/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import MovieListItem from '../Movie/MovieListItem.vue';

export default {
  name : 'CurrentMovieList',
  components :{
    MovieListItem,
  },
  data(){
    return {
      
    }
  },
  computed:{
    ...mapGetters(['currentMovies']),
  },
  created(){
    this.getCurrentMovie()
  },
  methods:{
    getCurrentMovie(){
      this.$store.dispatch('getCurrentMovies')
    }
  }
}
</script>

<style>

</style>