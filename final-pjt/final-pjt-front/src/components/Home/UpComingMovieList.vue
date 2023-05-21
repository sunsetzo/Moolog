<template>
  <div>
    <h1>상영 예정 영화</h1>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name : 'UpComingMovieList',
  components :{
  },
  computed:{
    ...mapGetters(['upcomingMovies']),
  },
}
</script>

<style>

</style>