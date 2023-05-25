<template>
  <div>
     <h2 style="color:white; margin-top:30px">User Profile</h2>
      <UserProfile/>
    <v-app>
      <UserLikeMovie/>
      <UserReview/>
    </v-app>
  </div>
</template>

<script>
import UserProfile from '@/components/UserPage/UserProfile.vue';
import UserLikeMovie from '@/components/UserPage/UserLikeMovie.vue';
import UserReview from '@/components/UserPage/UserReview.vue';

export default {
  name : 'UserPageView',
  components:{
    UserProfile,
    UserLikeMovie,
    UserReview

  }
}
</script>

<style scoped>

</style>