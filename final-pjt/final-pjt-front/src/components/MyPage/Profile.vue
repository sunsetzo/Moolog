<template>
  <div class="profile">
    <div>
      <img :src="userImg" alt="profile img">
    </div>
    <div>
      <h1>{{ nickname }}</h1>
      <p>팔로워 수: {{ followersCount }}</p>
      <p>팔로잉 수: {{ followingsCount }}</p>
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
      isFollowing: false       // 현재 사용자가 팔로우 중인지 여부
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
  }
}
</script>

<style scoped>
.profile{
  display: flex;
  justify-content: space-around;
}
img {
  width: 300px;
  height: 300px;
}
</style>