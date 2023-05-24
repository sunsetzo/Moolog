<template>
  <div>
    <p>전체 영화 목록</p>
    <div class="astrodivider">
      <div class="astrodividermask"></div>
    </div>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/Movie/MovieList.vue';

export default {
  name : 'MovieView',
  components:{
    MovieList
  },
}
</script>

<style scoped>
p {
  color: whitesmoke;
  font-size: 25px;
  margin: 10px;
  margin-bottom: 15px;
}

.astrodivider {
  margin:auto;
  width:100%; 
  max-width: 100%;
  position:relative;
}

.astrodividermask { 
    overflow:hidden; height:20px; 
}

.astrodividermask:after { 
      content:''; 
      display:block; margin:-25px auto 0;
      width:100%; height:25px;  
        border-radius:125px / 12px;
       box-shadow:0 0 8px #4DD0E1;
}

.astrodivider i {
    position:absolute;
    top:4px; bottom:4px;
    left:4px; right:4px;
    border-radius:100%;
    border:1px dashed #68beaa;
    text-align:center;
    line-height:40px;
    font-style:normal;
     color:#4DD0E1;
}
</style>