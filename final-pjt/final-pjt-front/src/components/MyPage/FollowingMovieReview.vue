<template>
  <div>
    <h3>My Following Recent Review</h3>
    <p>{{ FollowingReview }}</p>
    <v-main class="main-container">
      <v-carousel
      class="carousel-container"
      hide-delimiters>
        <template v-for="(item, index) in FollowingReview">
          <v-carousel-item
            v-if="(index + 1) % columns === 2 || columns === 2"
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
                        <div class="image-title" style="background-color: #212121; margin: 0px 0px 30px;">
                          <p>{{ FollowingReview[+index + i].content }}</p>
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
      myFollowing : [],
      FollowingReview : [],
    }
  },
  created(){
    this.myFollowing = this.userInfo.followings
    console.log(this.myFollowing)
    this.myFollowing.forEach((followId)=>{
      axios({
        method:'get',
        url : `${API_URL}/accounts/profile/${followId}/`
      })
      .then((res)=>{
        const popularReview = res.data.popularreview_set[res.data.popularreview_set.length-1]
        const upcomingReview = res.data.upcomingreview_set[res.data.upcomingreview_set.length-1]
        const nowplayingReview = res.data.nowplayingreview_set[res.data.nowplayingreview_set.length-1]
        this.FollowingReview.push(popularReview, nowplayingReview, upcomingReview)
      })
    })
  },
}
</script>

<style scoped>

</style>