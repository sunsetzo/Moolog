<template>
  <div>
      유저 페이지
      <UserProfile/>
      <UserLikeMovie/>
      <UserReview/>
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