<template>
  <div>
    내가 리뷰단 영화
    <v-main class="main-container">
      <v-carousel
      class="carousel-container"
      hide-delimiters>
        <template v-for="(item, index) in myReviewMovie">
          <v-carousel-item
            v-if="(index + 1) % columns === 2 || columns === 2"
            :key="index"
          >
            <v-row class="flex-nowrap" style="height: 100%">
              <template v-for="(n, i) in columns">
                <v-col :key="i">
                  <v-sheet
                    v-if="(+index + i) < myReviewMovie.length"
                    style="height: 330px; width: 300px; border-radius: 5px; background-color: #212121;"
                  >
                    <v-row class="fill-height" align="center" justify="center">
                      
                      <div class="image-container" style="color: white;">
                        <v-img
                        :src="`https://www.themoviedb.org/t/p/w533_and_h300_bestv2${myReviewMovie[+index + i].poster}`"
                        :alt="myReviewMovie[+index + i].title" 
                        style="width:300px; height: 130px; border-top-left-radius: 5px; border-top-right-radius: 5px;"
                        ></v-img>
                        <div class="image-title" style="background-color: #212121; margin: 0px 0px 30px;">
                          <p style="font-size: large; padding-bottom: 10px; padding-right: 8px; margin:0px;
                          text-align: right;">{{ myReviewMovie[+index + i].movieTitle }}</p>
                          <p style="text-align: left; margin-left: 10px;"><i class="fa-solid fa-quote-left fa-lg" style="color:#7E57C2;"></i></p>
                          <p style="font-size: medium;">"{{ myReviewMovie[+index + i].reviewContent }}"</p>
                          <p style="text-align: right; margin-right: 10px;"><i class="fa-solid fa-quote-right fa-lg" style="color:#7E57C2;"></i></p>
                          <p>{{ myReviewMovie[+index + i].reviewDate.slice(2,4)+'.'
                          +myReviewMovie[+index + i].reviewDate.slice(5,7) + '.' 
                          +myReviewMovie[+index + i].reviewDate.slice(8,10)
                          + ' ' + myReviewMovie[+index + i].reviewDate.slice(11,13) + ':'
                          + myReviewMovie[+index + i].reviewDate.slice(14,16)}}</p>
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
  name : 'MyReviewMovie',
  computed:{
    ...mapGetters(['userInfo']),
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

      return 3;
    }
  },
  data(){
    return{
      myReviewMovie : [],
    }
  },
  created(){
    this.userInfo.nowplayingreview_set.forEach((el)=>{
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
        this.myReviewMovie.push({reviewContent, movieTitle, reviewDate, poster})
      })
    })
    this.userInfo.upcomingreview_set.forEach((el)=>{
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
        this.myReviewMovie.push({reviewContent, movieTitle, reviewDate, poster})
      })
    })
    this.userInfo.popularreview_set.forEach((el)=>{
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
        this.myReviewMovie.push({reviewContent, movieTitle, reviewDate, poster})
      })
    })
  },
}
</script>

<style scoped>

</style>
