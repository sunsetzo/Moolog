<template>
  <div>
    팔로잉한 사람들의 가장 최신 리뷰
    <p>{{ FollowingReview }}</p>
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
        const popularReview = res.data.popularreview_set[-1]
        const upcomingReview = res.data.upcomingreview_set[-1]
        const nowplayingReview = res.data.nowplayingreview_set[-1]
        this.FollowingReview.push({popularReview, nowplayingReview, upcomingReview})
        console.log(this.FollowingReview)
      })
    })
  }
}
</script>

<style>

</style>