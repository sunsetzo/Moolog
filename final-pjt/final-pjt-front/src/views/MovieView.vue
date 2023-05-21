<template>
  <div>
    <h2>Movieview</h2>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/Movie/MovieList.vue';

export default {
  name : 'MovieView',
  components:{
    MovieList
  },
}
</script>

<style>

</style>