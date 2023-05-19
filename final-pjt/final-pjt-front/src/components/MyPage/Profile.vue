<template>
  <div class="profile">
    <div>
      <img :src="userinfo.user_image" alt="profile img">
    </div>
    <div>
      <h1>{{ username }}</h1>
      <p>팔로워 수: {{ followersCount }}</p>
      <p>팔로잉 수: {{ followingsCount }}</p>
      <button @click="toggleFollow">
        {{ isFollowing ? '언팔로우' : '팔로우' }}
      </button>
    </div>  
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name : 'ProFile',
  data() {
    return {
      username: '',            // 사용자 이름
      followersCount: 0,       // 팔로워 수
      followingsCount: 0,      // 팔로잉 수
      isFollowing: false       // 현재 사용자가 팔로우 중인지 여부
    };
  },
  mounted() {
    // 사용자 정보 및 팔로우/팔로잉 수를 가져오는 API 요청
    this.getUserData();
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
      axios.post('/api/follow/', { username: this.username })
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
      axios.post('http://127.0.0.1:8000/accounts/follow/', { username: this.username })
        .then(response => {
          console.log(response)
          this.isFollowing = false;
          this.followersCount--;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getUserData() {
      // 사용자 정보 및 팔로우/팔로잉 수를 가져오는 API 요청
      axios.get(`http://127.0.0.1:8000/accounts/follow/${this.username}`)
        .then(response => {
          this.username = response.data.username;
          this.followersCount = response.data.followers_count;
          this.followingsCount = response.data.followings_count;
          this.isFollowing = response.data.is_following;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
}
</script>

<style>
.profile{
  display: flex;
  justify-content: space-around;
}
</style>