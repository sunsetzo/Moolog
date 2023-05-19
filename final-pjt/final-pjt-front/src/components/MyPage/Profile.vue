<template>
  <div class="profile">
    <div>
      <img :src="userinfo.user_image" alt="profile img">
    </div>
    <div>
      <p>{{ userinfo.nickname }}</p>
      <button v-if="!isCurrentUser" @click="editprofile">프로필 수정</button>
      <button v-if="isCurrentUser" disabled>본인 페이지</button>
      <button v-if="!isCurrentUser && !isFollowing" @click="follow">팔로우</button>
      <button v-if="!isCurrentUser && isFollowing" @click="unfollow">언팔로우</button>
    </div>  
  </div>
</template>

<script>
export default {
  name : 'ProFile',
  computed: {
    userinfo() {
      return this.$store.state.user
    },
    isCurrentUser(){
      const currentUser = this.$store.state.login.user
      return currentUser && currentUser.id === this.userinfo.id
    }
  },
  created(){
    this.getFollow()
  },
  methods:{
    editprofile(){
      this.$router.push({name:'profileedit'})
    },
    getFollow(){
      this.$store.dispatch('getFollow')
    },
    
  }
}
</script>

<style>
.profile{
  display: flex;
  justify-content: space-around;
}
</style>