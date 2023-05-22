<template>
<div>
    <h1>{{movie.title}}</h1>
    <!-- 영화 포스터 및 타이틀 -->
    <div>
    <div>
        <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`" alt="포스터 이미지">
    </div>
    <div>
        <div>
        줄거리 : {{ movie.overview }}
        </div>
    </div>
    </div>
    <!-- 영화 예고편 영상 -->
    <div>
    영화 예고편 유튜브 api
    </div>
    <!-- 영화 리뷰 -->
    <div>
    영화 리뷰
    <CurrentMovieReview/>
    </div>
</div>
</template>

<script>
import CurrentMovieReview from '../components/Movie/CurrentMovieReview.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000/api/v1'

export default {
name : 'CurrentMovieDetail',
components:{
  CurrentMovieReview
},
data(){
    return{
        movie : []
    }
},
created(){
    this.getMovieDetail()
},
methods:{
    getMovieDetail(){
        axios({
            methods:'get',
            url:`${API_URL}/now_playing_movies/${this.$route.params.id}`
        })
        .then((res)=>{
            // console.log(res)
            this.movie = res.data
            console.log(this.movie)
        })
        .catch((err)=>{
            console.log('getMovieDetail err', err)
        })
    }
}
}
</script>

<style>

</style>