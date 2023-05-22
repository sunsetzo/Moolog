<template>
  <div >
    <img :src="posterURL" alt="" class="slide-card">
  </div>  
</template>

<script>
export default {
  name:'SlideCard',
  props:{
    movie : Object
  },
  data(){
        return{
            moviePosterUrl : 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'
        }
    },
    computed:{
        posterURL() {
            return this.moviePosterUrl + this.movie.poster_path
        }
    }


}
</script>

<style>
.slide-card-set{
  width: 210px;
  height: 310px;
}
.slide-card{
  width: 200px;
  height: 300px;
}
</style>