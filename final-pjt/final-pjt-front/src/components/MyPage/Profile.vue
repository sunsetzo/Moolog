<template>
  <div class="profile">
    <div>
      <img :src="userImg" alt="profile img" style="border-radius: 50%; margin-top: 30px; ">
      <br><br>
      <h1>{{ nickname }}</h1>
      <router-link :to="{name:'profileedit'}">
        <v-btn
        elevation="2" color="#7c5091"
        style="color:white; width:200px; font-weight: bold; margin-bottom: 20px;">
        프로필 수정</v-btn>
      </router-link>
    </div>
    <div class="user-info">
      <div class="information"><i class="fa-solid fa-film fa-2xl icon" style="color: #7c5091;"></i><span>{{ likeMovie }}</span><p>영화</p></div>
      <div class="horizion"></div>
      <div class="information"><i class="fa-solid fa-comments fa-2xl icon" style="color: #7c5091;"></i><span>{{ comment }}</span><p>리뷰</p></div>
      <div class="horizion"></div>
      <div class="information"><i class="fa-solid fa-user-group fa-2xl icon" style="color: #7c5091;"></i><span>{{ followersCount }}</span><p>팔로워</p></div>
      <div class="horizion"></div>
      <div class="information"><i class="fa-solid fa-user-plus fa-2xl icon" style="color: #7c5091;"></i><span>{{ followingsCount }}</span><p>팔로잉</p></div>
    </div>  
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name : 'ProFile',
  data() {
    return {
      userinfo : this.$store.state.user,
      nickname: this.$store.state.user.nickname,            // 사용자 이름
      followersCount: this.$store.state.user.followers_count,       // 팔로워 수
      followingsCount: this.$store.state.user.followings_count,      // 팔로잉 수
      isFollowing: false,       // 현재 사용자가 팔로우 중인지 여부
      likeMovie:0,
      comment:0
    };
  },
  computed:{
    ...mapGetters(['userInfo']),
    isCurrentUser() {
      return this.$store.state.user.pk === this.userinfo.pk;
    },
    userImg(){
      if (!this.userInfo.user_image){
        return 'http://127.0.0.1:8000/media/profile_images/user_img.png'
      }
      return this.userInfo.user_image
    }
  
  },
  methods: {
  },
  created(){
    this.likeMovie = (this.userInfo.like_now_playing_movies.length
    + this.userInfo.like_upcoming_movies.length + this.userInfo.like_popular_movies.length)
  
    this.comment = (this.userInfo.nowplayingreview_set.length
    + this.userInfo.upcomingreview_set.length + this.userInfo.popularreview_set.length) 
  }
}
</script>

<style scoped>
.profile{
  background: linear-gradient( rgb(0, 0, 0), #513581, rgb(0, 0, 0));
  box-shadow:-2 1 5px #7E57C2;
  margin: auto;
  margin-top: 50px;
  border-radius: 10px;
}
img {
  width: 300px;
  height: 300px;
}
.user-info{
  display: flex;
  justify-content: space-evenly;
}
.information{
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  align-content: stretch;
}
.horizion{
  width: 2px;
  height: 130px;
  background-color: #2f2148;
  box-shadow:0 0 8px #7E57C2;
  margin-top: 10px;
}.icon{
  margin-bottom: 17px;
}
</style>