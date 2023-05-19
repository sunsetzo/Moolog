<template>
  <div>
    <ProFile/>
    <MyLoveMovie/>
    <MyReviewMovie/>
    <FollowingMovieReview/>
  </div>
</template>

<script>
import ProFile from '@/components/MyPage/ProFile.vue';
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

<style>

</style>