<template>
  <div class="profile">
    <div>
      <img :src="userinfo.user_image" alt="profile img">
    </div>
    <div>
      <h1>{{ nickname }}</h1>
      <p>팔로워 수: {{ followersCount }}</p>
      <p>팔로잉 수: {{ followingsCount }}</p>
      <button v-if="!isCurrentUser" @click="toggleFollow">
        {{ isFollowing ? '언팔로우' : '팔로우' }}
      </button>
    </div>  
  </div>
</template>

<script>
import axios from 'axios';
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
    ...mapGetters(['currentUser']),
    isCurrentUser() {
      return this.$store.state.user.pk === this.userinfo.pk;
    }
  },
  methods: {
    toggleFollow() {
      // 팔로우/언팔로우 버튼 클릭 시 실행되는 함수
      if (this.isFollowing) {
        this.unfollowUser();
      } else {
        this.followUser();
      }
    },
    followUser() {
      // 팔로우 API 요청
      axios.post('http://127.0.0.1:8000/accounts/follow/:userpk', { userpk: this.userinfo.pk })
        .then((res) => {
          console.log(res)
          this.isFollowing = true;
          this.followersCount++;
        })
        .catch(error => {
          console.error(error);
        });
    },
    unfollowUser() {
      // 언팔로우 API 요청
      axios.post('http://127.0.0.1:8000/accounts/follow/:userpk', { userpk: this.userinfo.pk })
        .then(response => {
          console.log(response)
          this.isFollowing = false;
          this.followersCount--;
        })
        .catch(error => {
          console.error(error);
        });
    },
  }
}
</script>

<style>
.profile{
  display: flex;
  justify-content: space-around;
}
img {
  width: 300px;
  height: 300px;
}
</style>