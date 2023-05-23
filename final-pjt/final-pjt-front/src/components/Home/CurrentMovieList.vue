<template>
  <div>
    <h2>현재 상영작</h2>
    <v-app class="app-container">
      <v-main class="main-container">
        <v-carousel
          class="carousel-container"
          hide-delimiters
        >
          <template v-for="(item, index) in currentMovies">
            <v-carousel-item
              v-if="(index + 1) % columns === 1 || columns === 1"
              :key="index"
              @mouseenter="showInfo(index)"
              @mouseleave="hideInfo(index)"
            >
              <v-row class="flex-nowrap" style="height: 100%">
                <template v-for="(n, i) in columns">
                  <v-col :key="i">
                    <v-sheet
                      v-if="(+index + i) < currentMovies.length"
                    >
                      <v-row class="fill-height" align="center" justify="center">
                        <div class="position-relative">
                          <v-img
                            :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${currentMovies[+index + i].poster_path}`"
                            :alt="currentMovies[+index + i].title"
                            height="100%"
                            class="imgJanela hoverIMG"
                          ></v-img>
                          <div class="position-absolute top-50 start-50 translate-middle w-100" v-show="visibleIndex === index">
                            <div>
                              <p style="color:white;">{{ currentMovies[+index + i].title }}</p>
                              <div>
                                <i class="fa-solid fa-star mb-3" style="color: #ff6a38;"><span>   {{ currentMovies[+index + i].vote_avg }}</span></i>
                              </div>
                            </div>
                            <div>
                              <router-link :to="{name:'currentmovie', params:{id:currentMovies[+index + i].id}}">
                                <v-btn outlined large elevation="7" color="#FFFFFF">
                                  <span class="me-1">상세보기</span>
                                  <v-icon small>fas fa-search</v-icon>
                                </v-btn>
                              </router-link>
                            </div>
                          </div>
                        </div>
                      </v-row>
                    </v-sheet>
                  </v-col>
                </template>
              </v-row>
            </v-carousel-item>
          </template>
        </v-carousel>
      </v-main>
    </v-app>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name : 'CurrentMovieList',
  data() {
    return {
      isVisible :false,
      visibleIndex: null,
    };
  },
  computed:{
    ...mapGetters(['currentMovies']),
    currentMoviePosetURL(){
      return this.currentMovies
    },
    columns() {
      if (this.$vuetify.breakpoint.xl) {
        return 6;
      }

      if (this.$vuetify.breakpoint.lg) {
        return 4;
      }

      if (this.$vuetify.breakpoint.md) {
        return 3;
      }

      return 1;
    }
  },
  created(){
    this.getCurrentMovies()
  },
  methods:{
    getCurrentMovies(){
      this.$store.dispatch('getCurrentMovies')
    },
    showInfo(index) {
      this.visibleIndex = index;
    },
    hideInfo() {
      this.visibleIndex = null;
    },
  }

};
</script>

<style scoped>
.app-container {
  height: 600px; /* 원하는 높이로 설정 */
}
.main-container {
  height: 100%; /* 부모 요소인 v-app의 높이에 맞춤 */
}
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
