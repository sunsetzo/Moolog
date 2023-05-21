<template>
  <div>
    <h1>현재 상영 영화</h1>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name : 'CurrentMovieList',
  components :{
  },
  computed:{
    ...mapGetters(['currentMovies']),
  },
  // created(){
  //   this.getCurrentMovie()
  // },
  // methods:{
  //   getCurrentMovie(){
  //     this.$store.dispatch('getCurrentMovie')
  //   }
  // }
}
</script>

<style>

</style>