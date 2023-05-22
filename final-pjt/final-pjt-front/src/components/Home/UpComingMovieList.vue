<template>
  <div>
    <h2>상영 예정 영화</h2>
    <v-sheet
      class="mx-auto"
      elevation="8"
      max-width="1950"
      color="black"
    >
      <v-slide-group
        color="white"
        v-model="model"
        class="pa-4"
        selected-class="bg-success"
        prev-icon="mdi-minus"
        next-icon="mdi-plus"
        show-arrows
      >
        <v-slide-item
          v-for="movie in upcomingMovies"
          :key="movie.id"
          v-slot="{ active, toggle }">
          <v-hover v-slot="{ hover }">
            <v-card
              color="black"
              class="mx-auto my-auto"
              height="460"
              width="310"
              :class="{ 'bg-dark': active }"
              @click="toggle"
            >
            
            <v-img
            :aspect-ratio="3/4"
            :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`" alt="current_movie_poster" 
            class="imgJanela hoverIMG">
            </v-img>
            <v-btn v-if="hover"
            center
              elevation="6">
              <router-link :to="{name:'upcomingmovie', params:{id:movie?.id}}">상세보기</router-link>
              </v-btn>
              <div class="d-flex fill-height align-center justify-center">
                <v-scale-transition>
                  <v-icon
                    v-if="active"
                    color="white"
                    size="48"
                    @click.stop="toggle"
                    >
                  </v-icon>
                </v-scale-transition>
              </div>
            </v-card>
        </v-hover>
        </v-slide-item>
      </v-slide-group>
    </v-sheet>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name : 'UpComingMovieList',
  data(){
    return{
      model:null,
    }
  },
  components :{
  },
  computed:{
    ...mapGetters(['upcomingMovies']),
  },
  created(){
    this.getUpComingMovie()
  },
  methods:{
    getUpComingMovie(){
      this.$store.dispatch('getUpComingMovies')
    }
  }
}
</script>

<style>
.upcomingMoviePoster{
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