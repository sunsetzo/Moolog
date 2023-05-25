<template>
  <div>
    <h3>My Following Recent Review</h3>
    <v-main class="main-container">
      <v-carousel
      class="carousel-container"
      hide-delimiters>
        <template v-for="(item, index) in FollowingReview">
          <v-carousel-item
            v-if="(index + 1) % columns === 1 || columns === 1"
            :key="index"
          >
            <v-row class="flex-nowrap" style="height: 100%">
              <template v-for="(n, i) in columns">
                <v-col :key="i">
                  <v-sheet
                    v-if="(+index + i) < FollowingReview.length"
                    style="height: 330px; width: 300px; border-radius: 5px; background-color: #212121;">
                    <v-row class="fill-height" align="center" justify="center">
                      <div class="image-container" style="color: white;">
                        <div style="margin-top:20px">
                          <router-link :to="{name:'userprofile', params:{userid:FollowingReview[+index+i].reviewUserPk}}">
                            <i class="fa-solid fa-user-astronaut fa-xl" style="color: #57a3a8;"></i>
                            <i class="fa-solid fa-comment fa-xl" style="color: #57a3a8;"></i>
                          </router-link>
                        </div>
                        <div class="image-title" style="background-color: #212121; margin: 10px 0px 20px;
                        display: flex; flex-direction: column; align-content: space-around;">
                          <p style="font-size:large; font-weight: bold; margin-top: 10px; margin-bottom: 40px;">
                            {{ FollowingReview[+index + i].movieTitle }}</p>
                          <p style="text-align: left; margin-left: 10px;"><i class="fa-solid fa-quote-left fa-lg" style="color:#57a3a8;"></i></p>
                          <p>{{ FollowingReview[+index + i].reviewContent }}</p>
                          <p style="text-align: right; margin-right: 10px;"><i class="fa-solid fa-quote-right fa-lg" style="color:#57a3a8;"></i></p>
                          <p style="margin-top:30px">{{ FollowingReview[+index + i].reviewCreate.slice(2,4)+'.'
                          +FollowingReview[+index + i].reviewCreate.slice(5,7) + '.' 
                          +FollowingReview[+index + i].reviewCreate.slice(8,10)
                          + ' ' + FollowingReview[+index + i].reviewCreate.slice(11,13) + ':'
                          + FollowingReview[+index + i].reviewCreate.slice(14,16)}}</p>
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
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'FollowingMovieReview',
  computed:{
    ...mapGetters(['userInfo']),
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
  data(){
    return{
      myFollowing : [],
      FollowingReview : [],
    }
  },
  created(){
    this.myFollowing = this.userInfo.followings
    this.myFollowing.forEach((followId)=>{
      axios({
        method:'get',
        url : `${API_URL}/accounts/profile/${followId}/`
      })
      .then((res)=>{
        const popularReview = res.data.popularreview_set[res.data.popularreview_set.length-1]
        const movieId = popularReview.movie
        if (movieId){
          axios({
            method:'get',
            url : `${API_URL}/api/v1/popular_movies/${movieId}`
          })
          .then((res)=>{
            const movieTitle = res.data.title
            const reviewContent = popularReview.content
            const reviewCreate = popularReview.created_at
            const reviewUserPk = popularReview.user
            this.FollowingReview.push({movieTitle, reviewContent, reviewCreate, reviewUserPk})
          })
          return
        }

        const upcomingReview = res.data.upcomingreview_set[res.data.upcomingreview_set.length-1]
        if (movieId){
          axios({
            method:'get',
            url : `${API_URL}/api/v1/upcoming_movies/${movieId}`
          })
          .then((res)=>{
            const movieTitle = res.data.title
            const reviewContent = upcomingReview.content
            const reviewCreate = upcomingReview.created_at
            const reviewUserPk = upcomingReview.user
            this.FollowingReview.push({movieTitle, reviewContent, reviewCreate, reviewUserPk})
          })
          return
        }

        const nowplayingReview = res.data.nowplayingreview_set[res.data.nowplayingreview_set.length-1]
        if (movieId){
          axios({
            method:'get',
            url : `${API_URL}/api/v1/now_playing_movies/${movieId}`
          })
          .then((res)=>{
            const movieTitle = res.data.title
            const reviewContent = nowplayingReview.content
            const reviewCreate = nowplayingReview.created_at
            const reviewUserPk = nowplayingReview.user
            this.FollowingReview.push({movieTitle, reviewContent, reviewCreate, reviewUserPk})
          })
          return
        }

        console.log(this.FollowingReview)
      })
    })
  },
}
</script>

<style scoped>

</style>