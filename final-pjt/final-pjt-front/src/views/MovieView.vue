<template>
  <div>
    <h2>전체 영화 목록</h2>
    <div class="divider"></div>
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

<style scoped>
h2 {
  color: whitesmoke;
  margin-bottom: 10px;
}

.divider {
  height: 2px;
  background-color: white;
  margin-bottom: 15px;
  margin-left: 5px;
  margin-right: 5px;
}
</style>