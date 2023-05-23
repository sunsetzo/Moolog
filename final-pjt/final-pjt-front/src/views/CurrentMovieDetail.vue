<template>
<div>
    <h1>{{movie?.title}}</h1>
    <!-- 영화 포스터 및 타이틀 -->
    <div>
    <div>
        <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie?.poster_path}`" alt="포스터 이미지">
    </div>
    <div>
        <div>
        <span>줄거리 : {{ movie?.overview }}</span>
        </div>
        <div>
            <!-- 영화 좋아요 -->
            <button @click="likeMovie">
                {{ isLike && myLike ? '좋아요 취소' : '좋아요'}} </button>
            <br>
            <span>좋아요 수 : {{ movie?.like_users.length }}</span>
        </div>
    </div>
    </div>
    <!-- 영화 예고편 영상 -->
    <div>
    영화 예고편 유튜브
    <iframe :src="videoURL" frameborder="0" width="500px" height="300px"></iframe>
    </div>
    <!-- 영화 리뷰 -->
    <div>
    영화 리뷰
    <p v-for="(review, idx) in reviews" :key="idx">
        <span>별점 : {{ review.rate }}</span>
        <br>
        <span>{{ review.content }}</span>
    </p>
    
    <CurrentMovieReview/>
    </div>
</div>
</template>

<script>
import CurrentMovieReview from '../components/Movie/CurrentMovieReview.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000/api/v1'
// const YOUTUBE_KEY = 'AIzaSyBkdQF46yaw0HH0kpENBBanwFI1y1mGnhI'
// const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
name : 'CurrentMovieDetail',
components:{
  CurrentMovieReview
},
data(){
    return{
        movie : [],
        reviews : [],
        title : null,
        MovieTrailer : null,
        videoURL : null,
        myLike : false,
        isLike : false
    }
},
computed:{
    // myLike(){
    //     return
    // }
},
mounted(){
    this.getMovieDetail()
},
methods:{
    getMovieDetail(){
        axios({
            methods:'get',
            url:`${API_URL}/now_playing_movies/${this.$route.params.id}/`
        })
        .then((res)=>{
            console.log(res)
            this.movie = res.data
            this.reviews = res.data.nowplayingreview_set
            this.title = res.data.title + 'trailer'
            // console.log(this.movie)
            // this.getMovieTrailer()
        })
        .catch((err)=>{
            console.log('getMovieDetail err', err)
        })
    },
    // getMovieTrailer(){
    //     const params = {
    //         key : YOUTUBE_KEY,
    //         part : 'snippet',
    //         type:'video',
    //         q : this.title
    //     }
    //     axios({
    //         method:'get',
    //         url:YOUTUBE_URL,
    //         params,
    //     })
    //     .then(res=>{
    //         console.log(res)
    //         this.MovieTrailer = res.data.items[0]
    //         console.log(this.MovieTrailer)
    //         this.videoURL = `https://youtube.com/embed/${this.MovieTrailer.id.videoId}`
    //     })
    //     .catch(err=>{
    //         console.log(err)
    //     })
    // },
    likeMovie(){
        const token = this.$store.state.login.token
        axios({
            method:'post',
            url : `${API_URL}/now_playing_movies/${this.$route.params.id}/likes/`,
            headers:{
                Authorization: `Token ${token}`
            }
        })
        .then((res)=>{
            console.log(res)
            this.isLike = !this.isLike
        })
        .catch((err)=>{
            console.log(err)
        })
    }
}
}
</script>

<style>

</style>