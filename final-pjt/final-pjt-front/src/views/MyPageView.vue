<template>
  <div>
    <ProFile/>
    <v-app>
      <MyLoveMovie/>
      <MyReviewMovie/>
      <FollowingMovieReview/>
    </v-app>
  </div>
</template>

<script>
import ProFile from '@/components/MyPage/Profile.vue';
import MyLoveMovie from '@/components/MyPage/MyLoveMovie.vue';
import MyReviewMovie from '@/components/MyPage/MyReviewMovie.vue';
import FollowingMovieReview from '@/components/MyPage/FollowingMovieReview.vue';

export default {
  name : 'MyPageView',
  components:{
    ProFile,
    MyLoveMovie,
    MyReviewMovie,
    FollowingMovieReview,

  }
}
</script>

<style scoped>
* {
  color: whitesmoke;
}
</style>