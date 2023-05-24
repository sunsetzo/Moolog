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
        <span>줄거리 : {{ movie?.overview }}</span><br>
        <span>개봉일 : {{ movie?.release_date }}</span><br>
        장르 : <span v-for="(genre) in genres" :key="genre.id">{{ genre.name }}, </span>
        </div>
        <div>
            <!-- 영화 좋아요 -->
            <button @click="likeMovie">
                {{ (isLike || isMyLike) ? '좋아요' : '좋아요 취소'}} </button>
            <br>
            <span>좋아요 수 : {{ likeUserLength }}</span>
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
        <span><router-link :to="{name:userprofile, params:{id:review.user}} ">작성자 : {{ review.nickname }}</router-link></span>
        <span>별점 : {{ review.rate }}</span>
        <br>
        <span>{{ review.content }}</span>
    </p>
    
        <UpComingMovieReview/>
      </div>
    </div>
</template>

<script>
import UpComingMovieReview from '../components/Movie/UpComingMovieReview.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000/api/v1'
// const YOUTUBE_KEY = 'AIzaSyBkdQF46yaw0HH0kpENBBanwFI1y1mGnhI'
// const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
    name:'UpComingMovieDetail',
    components:{
        UpComingMovieReview
    },
    data(){
        return{
            movie : [],
            reviews:[],
            genres:[],
            title : null,
            MovieTrailer : null,
            videoURL : null,
            isLike : false,
            isMyLike : false,
            likeUserLength : 0,
        }
    },
    created(){
        this.getMovieDetail()
    },
    methods:{
        getMovieDetail(){
            axios({
                methods:'get',
                url:`${API_URL}/upcoming_movies/${this.$route.params.id}`
            })
            .then((res)=>{
                this.movie = res.data
                this.reviews = res.data.upcomingreview_set
                this.title = res.data.title + 'trailer'
                // this.getMovieTrailer() //유튜브
                this.likeUserLength = res.data.like_users.length
                this.genres = res.data.genres
                const user_pk = this.$store.state.user.pk
                if (this.movie.like_users.includes(user_pk)){
                    this.isMyLike = false
                    this.isLike = false
                }
                else{
                    this.isMyLike = true
                    this.isLike = true
                }
            })
            .catch((err)=>{
                console.log('getMovieDetail err', err)
            })
        },
    //     getMovieTrailer(){
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
            url : `${API_URL}/upcoming_movies/${this.$route.params.id}/likes/`,
            headers:{
                Authorization: `Token ${token}`
            }
        })
        .then((res)=>{
            console.log(res)
            this.isLike = !this.isLike
            if (this.isLike === false){
                this.likeUserLength ++
            }else{
                this.likeUserLength --
            }
        })
        .catch((err)=>{
            console.log(err)
        })
    },

    }
}
</script>

<style>

</style>