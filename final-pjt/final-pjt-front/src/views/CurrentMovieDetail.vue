<template>
<div class="currentMovieDetail">
    <img :src="`https://www.themoviedb.org/t/p/original/${movie?.backdrop_path}`" alt="배경 이미지" class="backgroundimg">
        <!-- 절대위치 주기 -->
        <div class="movie-info">
            <div class="col-6 col-md-4 info-img">
                <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie?.poster_path}`" alt="포스터 이미지">
            </div>
            <div class="col-6 col-md-8 info">
                <div class="movie-section">
                    <div class="movie-title">
                        <div style="text-align:left">
                            <span v-for="(genre) in genres" :key="genre.id">#{{ genre.name }} </span>
                        </div>
                        <h1 style="text-align:left" class="my-2">{{movie?.title}}</h1>
                        <p style="text-align:left">개봉 : {{ movie?.release_date }}</p>
                    </div>
                    <div class="heart">
                        <i v-show="isLike && isMyLike" @click="likeMovie" class="fa-regular fa-heart fa-xl" style="color: #c11a33"></i>
                        <i v-show="!isLike || !isMyLike" @click="likeMovie" class="fa-solid fa-heart fa-xl" style="color: #c11a33;"></i>
                        <br>
                        <span> {{ likeUserLength }}</span>
                    </div>
                </div>
                    <!-- divider -->
                    <div class="astrodivider">
                        <div class="astrodividermask"></div>
                    </div>
                <br>
                <div class="movie-overview">
                    <p style="text-align:left">{{ movie?.overview }}</p>
                </div>
            </div>
        </div>
        <!-- 영화 예고편 영상 -->
    <iframe :src="videoURL" frameborder="0" width="100%" height="800px" class="YTB"></iframe>
    <!-- 영화 리뷰 -->
    <div>
        <div class="review-box">
            <div v-for="(review, idx) in reviews" :key="idx">
                <div class="star-ratings review-rate">
                    <div 
                    class="star-ratings-fill space-x-2 text-lg"
                    :style="{ width: `${review.rate * 20}%` }"
                    >
                        <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
                    </div>
                    <div class="star-ratings-base space-x-2 text-lg">
                        <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
                    </div>
                </div>
                <div class="review-content">
                    <div class="review-user">
                        <router-link :to="{name:'userprofile', params:{userid:review.user}} "><i class="fa-solid fa-circle-user fa-2xl" style="color: #00a1b0"></i>
                            <br><br>
                        <span>{{ review.nickname }}</span></router-link>
                    </div>
                    
                    <div class="speech-bubble">{{ review.content }}</div>
                </div>
            </div>
        </div>
        
        <CurrentMovieReview/>
    </div>
</div>
</template>

<script>
import CurrentMovieReview from '../components/Movie/CurrentMovieReview.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api/v1'
const YOUTUBE_KEY = 'AIzaSyBkdQF46yaw0HH0kpENBBanwFI1y1mGnhI'
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
name : 'CurrentMovieDetail',
components:{
  CurrentMovieReview
},
data(){
    return{
        movie : [],
        reviews : [],
        genres:[],
        title : null,
        MovieTrailer : null,
        videoURL : null,
        isLike : false,
        isMyLike : false,
        likeUserLength : 0,
    }
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
            this.movie = res.data
            this.reviews = res.data.nowplayingreview_set
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
    getMovieTrailer(){
        const params = {
            key : YOUTUBE_KEY,
            part : 'snippet',
            type:'video',
            q : this.title
        }
        axios({
            method:'get',
            url:YOUTUBE_URL,
            params,
        })
        .then(res=>{
            this.MovieTrailer = res.data.items[0]
            this.videoURL = `https://youtube.com/embed/${this.MovieTrailer.id.videoId}`
        })
        .catch(err=>{
            console.log(err)
        })
    },
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
    },

}
</script>

<style scoped>
.currentMovieDetail{
    color: white;
    margin-top: 50px;
    width: 90%;
    margin: auto;
}
.backgroundimg{
    width: 100%;
    height: 40%;
    opacity: 0.3;
    filter: blur(3px);
    border-radius: 10px;
    margin-top: 50px;
}
.movie-info{
    height: 350px;
    display: flex;
    justify-content: space-around;
    position: static;
    top: 90%;
    transform: translateY(-50%);
}
.info-img{
    padding: 5px;
    width: 350px;

}
.info{
    padding: 10px;
    /* margin : 5px; */
}
.movie-section{
    display: flex;
    justify-content: space-between;
}
.movie-overview{
    margin-bottom: auto;
}
.movie-title{
    margin-right:auto;
}
.heart{
    align-self: center;
    margin-right: 20px;
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
.YTB{
    margin-top: 0px;
}
.speech-bubble {
    width: 400px;
	position: relative;
	background:#00a1b0;
	border-radius: .4em;
}
.speech-bubble:after {
	content: '';
	position: absolute;
	left: 0;
	top: 50%;
	width: 0;
	height: 0;
	border: 0.875em solid transparent;
	border-right-color: #00a1b0;
	border-left: 0;
	border-top: 0;
	margin-top: -0.437em;
	margin-left: -0.875em;
}
.review-box{
    width: 80%;
    margin-right: auto;
    margin-left: auto;
}
.review-rate{
    margin-top: 30px;
    margin-left : 370px;
    margin-bottom: 5px;
}
.review-user{
    align-self: auto;
    margin-right: 25px;
}
.review-content{
    display: flex;
    justify-content: first baseline;
}
div a {
  text-decoration: none;
  text-decoration-line: none;
  color: white;
}
.star-ratings {
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
 
.star-ratings-fill {
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
 
.star-ratings-base {
  z-index: 0;
  padding: 0;
}
</style>