<template>
  <div>
    <MovieListItem v-for="(movie) in Movies" :key="movie.id" :movie="movie"/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import MovieListItem from './MovieListItem.vue';

export default {
  name : 'MovieList',
  components:{
    MovieListItem
  },
  computed:{
    ...mapGetters(['Movies']),
  },
  created(){
    this.getMovie()
  },
  methods:{
    getMovie(){
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style>

</style>