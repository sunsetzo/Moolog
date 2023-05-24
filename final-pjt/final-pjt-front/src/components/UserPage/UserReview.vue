<template>
  <div>
    유저가 리뷰단 영화
    <v-app  class="app-container">
      <v-main class="main-container">
        <v-carousel
        class="carousel-container"
        hide-delimiters>
          <template v-for="(item, index) in UserReviewMovies">
            <v-carousel-item
              v-if="(index + 1) % columns === 1 || columns === 1"
              :key="index"
            >
              <v-row class="flex-nowrap" style="height: 100%">
                <template v-for="(n, i) in columns">
                  <v-col :key="i">
                    <v-sheet
                      v-if="(+index + i) < UserReviewMovies.length"
                    >
                      <v-row class="fill-height" align="center" justify="center">
                        
                        <div class="image-container">
                          <div class="image-title">
                            {{ UserReviewMovies[+index + i].movieTitle }}
                            <br>
                            {{ UserReviewMovies[+index + i].reviewContent }}
                            <br>
                            {{ UserReviewMovies[+index + i].reviewDate }}
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
import { mapGetters } from 'vuex'
import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'UserReview',
  computed:{
    ...mapGetters(['userprofile']),
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
  data(){
    return{
      UserReviewMovies : [],
    }
  },
  created(){
    this.userprofile.nowplayingreview_set.forEach((el)=>{
      const movieId = el.movie
      const reviewContent = el.content
      const reviewDate = el.created_at
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/now_playing_movies/${movieId}/`
      })
      .then((res)=>{
        const movieTitle = res.data.title
        this.UserReviewMovies.push({reviewContent, movieTitle, reviewDate})
      })
    })
    this.userprofile.upcomingreview_set.forEach((el)=>{
      const movieId = el.movie
      const reviewContent = el.content
      const reviewDate = el.created_at
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/upcoming_movies/${movieId}/`
      })
      .then((res)=>{
        const movieTitle = res.data.title
        this.UserReviewMovies.push({reviewContent, movieTitle, reviewDate})
      })
    })
    this.userprofile.popularreview_set.forEach((el)=>{
      const movieId = el.movie
      const reviewContent = el.content
      const reviewDate = el.created_at
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/popular_movies/${movieId}/`
      })
      .then((res)=>{
        const movieTitle = res.data.title
        this.UserReviewMovies.push({reviewContent, movieTitle, reviewDate})
      })
    })
    // console.log(this.myReviewMovie)
  },
}
</script>

<style scoped>
.app-container {
  height: 600px; /* 원하는 높이로 설정 */
}
.main-container {
  height: 100%; /* 부모 요소인 v-app의 높이에 맞춤 */
}
.carousel-container{
  width: 2000px;
  margin: auto;
}
.info-sheet {
  width: 300px;
  height: 400px;
}
</style>
