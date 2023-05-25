<template>
  <div>
    <div class="d-flex ms-2 text-color section-title" style="color: #4DD0E1;">
            <span>Up</span>
            <span>coming</span>
            <span class="ms-1">Mo</span>
            <span>vies</span>
    </div>
    <v-main class="main-container">
      <v-carousel
        class="carousel-container"
        hide-delimiters
      >
        <template v-for="(item, index) in upcomingMovies">
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
                    v-if="(+index + i) < upcomingMovies.length"
                  >
                    <v-row class="fill-height" align="center" justify="center">
                      <div class="position-relative">
                        <v-img
                          :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${upcomingMovies[+index + i].poster_path}`"
                          :alt="upcomingMovies[+index + i].title"
                          height="100%"
                          class="imgJanela hoverIMG"
                        ></v-img>
                        <div class="position-absolute top-50 start-50 translate-middle w-100">
                        <div  v-show="visibleIndex === index">
                          <p style="color:white;">{{ upcomingMovies[+index + i].title }}</p>
                          <div>
                            <i class="fa-solid fa-star mb-3" style="color: #ff6a38;"><span>   {{ upcomingMovies[+index + i].vote_avg }}</span></i>
                          </div>
                        </div>
                        <div>
                          <router-link :to="{name:'upcomingmovie', params:{id:upcomingMovies[+index + i].id}}">
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
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name : 'UpComingMovieList',
  data() {
    return {
      isVisible :false,
      visibleIndex: null,
    };
  },
  computed:{
    ...mapGetters(['upcomingMovies']),
    upcomingMoviesPosetURL(){
      return this.upcomingMovies
    },
    columns() {
      if (this.$vuetify.breakpoint.xl) {
        return 6;
      }

      if (this.$vuetify.breakpoint.lg) {
        return 6;
      }

      if (this.$vuetify.breakpoint.md) {
        return 3;
      }

      return 3;
    }
  },
  created(){
    this.getupcomingMovies()
  },
  methods:{
    getupcomingMovies(){
      this.$store.dispatch('getUpComingMovies')
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
.upcomingMoviesPoster{
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

/* Fonts at: https://www.google.com/fonts */
@import url('https://fonts.googleapis.com/css?family=Pathway+Gothic+One');

.section-title {
  font-family: 'Pathway Gothic One', sans-serif;
  font-size: 35px;
  position: relative;
  letter-spacing: -2px;
  color: #4DD0E1;
}

.section-title span:before {
  content: '';
  height: 1px;
  position: absolute;
  bottom: 7px;
  background: #4DD0E1;
  width: 0%;
  animation: voila 1s forwards linear;
}

.section-title span:nth-child(2) {
  opacity: .75;
}

.section-title span:nth-child(3) {
  opacity: .5;
}

.section-title span:nth-child(4) {
  opacity: .25;
}

@keyframes voila {
  to { width: 100%; }
}
</style>
