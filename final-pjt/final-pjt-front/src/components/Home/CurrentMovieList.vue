<template>
  <div>
    <h3>현재 상영작</h3>
    <v-sheet
      class="mx-auto"
      elevation="8"
      max-width="800"
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
            class="ma-4"
            height="300"
            width="200"
            :class="{ 'bg-success': active }"
            @click="toggle"
          >
            <v-img
              v-if="movie.poster_path"
              :src="posterURL"
              aspect-ratio="1.5"
              :class="{ 'pointer': active }"
              @click.stop="toggle"
            ></v-img>
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
          </v-card>
        </v-slide-item>
      </v-slide-group>
    </v-sheet>
  </div>
</template>

<script>
export default {
  name: 'CurrentMovieList',
  data() {
    return {
      model: Array.from({ length: 6 }, (_, i) => i), // 초기에 active된 항목이 6개인 배열로 설정
      moviePosterUrl : 'https://www.themoviedb.org/t/p/w300_and_h450_bestv2'
    };
  },
  computed: {
    currentMovies() {
      return this.$store.getters.CurrentMovies;
    },
    posterURL() {
            return this.moviePosterUrl + this.movie.poster_path
        }

  },
  created() {
    this.getCurrentMovies();
  },
  methods: {
    getCurrentMovies() {
      this.$store.dispatch('getCurrentMovies');
    },
    // getImageUrl(posterPath) {
    //   console.log(posterPath)
    //   return `https://image.tmdb.org/t/p/w500${posterPath}`;
    // }
  }
};
</script>

<style>
.pointer {
  cursor: pointer;
}
</style>
