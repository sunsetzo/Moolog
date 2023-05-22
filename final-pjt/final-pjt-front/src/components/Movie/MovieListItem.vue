<template>
  <div>
    <div class="card h-100" @mouseenter="showButton" @mouseleave="hideButton">
      <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`" class="card-img-top position-relative" alt="movie_poster">
      <h5 class="position-absolute" style="left: 50%; transform: translateX(-50%);"
      v-show="isVisible"
      >{{ movie.title }}</h5>
      <button class="btn btn-primary position-absolute top-50 start-50 translate-middle"
      v-show="isVisible" style="transform: translateX(-50%);"
      >상세보기</button>
    </div>
  </div>
</template>

<script>
export default {
  name:'MovieListItem',
  props:{
    movie: Object
  },
  components: {

  },
  data() {
    return {
      isVisible: false
    }
  },
  methods: {
    showButton() {
      this.isVisible = true
    },
    hideButton() {
      this.isVisible = false
    }
  }

}
</script>

<style>
  img {
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
  }
  h5 {
    color: white;
  }
</style>