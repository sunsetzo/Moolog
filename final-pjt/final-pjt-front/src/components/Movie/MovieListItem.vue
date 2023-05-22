<template>
  <div>
    <v-card
    color="grey lighten-1"
    class="ma-4"
    height="100%"
    width="100%"
    @mouseenter="showInfo" @mouseleave="hideInfo">
      <v-img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`" alt="current_movie_poster" 
      :class="{ imgJanela: isVisible, hoverIMG : isVisible}"></v-img>
      <div class="position-absolute top-50 start-50 translate-middle">
        <h6 class="" v-if="isVisible">{{ movie.title }}</h6>
        <v-btn outlined large elevation="7" color="#FFFFFF"
        v-show="isVisible">
          <span class="me-1">상세보기</span>
          <v-icon small>fas fa-search</v-icon>
        </v-btn>
      </div>
    </v-card>
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
    showInfo() {
      this.isVisible = true
    },
    hideInfo() {
      this.isVisible = false
    }
  }

}
</script>

<style scoped>
.imgJanela{
    transform: scale(1.1);
}

.hoverIMG{
  -webkit-filter: grayscale(100%) blur(3px);
  filter: grayscale(100%) blur(3px);
}
</style>