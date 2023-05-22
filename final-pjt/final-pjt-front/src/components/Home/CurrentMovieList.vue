<template>
  <div>
    <h2>현재 상영작</h2>
    <v-sheet
      class="mx-auto"
      elevation="8"
      max-width="1950"
    >
      <v-slide-group
        v-model="model"
        class="pa-4"
        selected-class="bg-success"
        show-arrows
      >
        <v-slide-item
          v-for="movie in currentMovies"
          :key="movie.id"
          v-slot="{ active, toggle }"
        >
          <v-card
            color="grey lighten-1"
            class="ma-4"
            height="460"
            width="310"
            :class="{ 'bg-dark': active }"
            @click="toggle"
          >
          <v-img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`" alt="current_movie_poster" class="currentMoviePoster imgJanela hoverIMG"
          >
          </v-img>
            <div class="d-flex fill-height align-center justify-center">
              <v-scale-transition>
                <v-icon
                  v-if="active"
                  color="white"
                  size="48"
                  @click.stop="toggle"
                >
                  mdi-close-circle-outline
                </v-icon>
              </v-scale-transition>
            </div>
          </v-card>
        </v-slide-item>
      </v-slide-group>
    </v-sheet>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name : 'CurrentMovieList',
  data() {
    return {
      model: null,
    };
  },
  computed:{
    ...mapGetters(['currentMovies']),
    currentMoviePosetURL(){
      return this.currentMovies
    }
  },
  created(){
    this.getCurrentMovies()
  },
  methods:{
    getCurrentMovies(){
      this.$store.dispatch('getCurrentMovies')
    }
  }

};
</script>

<style scoped>
.currentMoviePoster{
  width: 300px;
  height: 450px;
  padding: 10px;
  margin-left: 5px;
}
.imgJanela:hover {
    transform: scale(1.1);
}
.hoverIMG{
  -webkit-filter: grayscale(0) blur(0);
  filter: grayscale(0) blur(0);
  -webkit-transition: .3s ease-in-out;
  transition: .3s ease-in-out;
}
.hoverIMG:hover{
  -webkit-filter: grayscale(100%) blur(3px);
  filter: grayscale(100%) blur(3px);
}
</style>
