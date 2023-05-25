<template>
  <div>
    <h3 style="margin-top:25px; color:white">User Reviews</h3>
      <v-main class="main-container">
        <v-carousel
        class="carousel-container"
        style="height:400px"
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
                      style="height: 330px; width: 300px; border-radius: 5px; background-color: #212121;"
                    >
                      <v-row class="fill-height" align="center" justify="center">
                        
                        <div class="image-container" style="color: white;">
                        <v-img
                        :src="`https://www.themoviedb.org/t/p/w533_and_h300_bestv2${UserReviewMovies[+index + i].poster}`"
                        :alt="UserReviewMovies[+index + i].title" 
                        style="width:300px; height: 130px; border-top-left-radius: 5px; border-top-right-radius: 5px;"
                        ></v-img>
                        <div class="image-title" style="background-color: #212121; margin: 0px 0px 30px;">
                          <p style="font-size: large; font-weight: bold; padding-bottom: 10px; padding-right: 8px; margin:0px;
                          text-align: right;">{{ UserReviewMovies[+index + i].movieTitle }}</p>
                          <p style="text-align: left; margin-left: 10px;"><i class="fa-solid fa-quote-left fa-lg" style="color:#7E57C2;"></i></p>
                          <p style="font-size: medium;">"{{ UserReviewMovies[+index + i].reviewContent }}"</p>
                          <p style="text-align: right; margin-right: 10px;"><i class="fa-solid fa-quote-right fa-lg" style="color:#7E57C2;"></i></p>
                          <p>{{ UserReviewMovies[+index + i].reviewDate.slice(2,4)+'.'
                          +UserReviewMovies[+index + i].reviewDate.slice(5,7) + '.' 
                          +UserReviewMovies[+index + i].reviewDate.slice(8,10)
                          + ' ' + UserReviewMovies[+index + i].reviewDate.slice(11,13) + ':'
                          + UserReviewMovies[+index + i].reviewDate.slice(14,16)}}</p>
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
        const poster = res.data.backdrop_path
        this.UserReviewMovies.push({reviewContent, movieTitle, reviewDate, poster})
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
        const poster = res.data.backdrop_path
        this.UserReviewMovies.push({reviewContent, movieTitle, reviewDate, poster})
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
        const poster = res.data.backdrop_path
        this.UserReviewMovies.push({reviewContent, movieTitle, reviewDate, poster})
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
