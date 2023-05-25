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
                    <p style="text-align:left;">{{ movie?.overview }}</p>
                </div>
            </div>
        </div>
        <!-- 영화 예고편 영상 -->
    <div style="width : 90%; height: 800px; margin:auto">
        <iframe :src="videoURL" frameborder="0" width="100%" height="100%" class="YTB"></iframe>
    </div>
    <!-- 영화 리뷰 -->
    <div style="margin-top:150px; background-color: #212121; border-radius: 5px; width:90%; margin:0px auto 60px;
    box-shadow: 1px 1px 10px #616161, -1px -1px 10px #616161;">
        <!-- 채팅방 상단 -->
        <div style="width:90%; height:100px; margin:auto; display: flex; justify-content: space-between; align-items: center;">
            <div><i class="fa-solid fa-chevron-left fa-2xl" style="color: #EEEEEE;"></i></div>
            <p style="text-align: center; font-size:28px; font-weight: 700; margin-top: 27px;">{{ movie?.title }}</p>
            <div><i class="fa-solid fa-bars fa-2xl" style="color: #EEEEEE;"></i></div>
        </div>
        <!-- 공지사항 -->
        <div style="height:80px; width:99%; margin:0px auto 20px; background-color: #EEEEEE; display: flex; justify-content: space-between; align-items: center;
        padding-bottom:10px; border-bottom-left-radius: 3px; border-bottom-right-radius: 3px;">
            <div style="margin-left:45px"><i class="fa-solid fa-bullhorn fa-2xl" style="color: #2d394d;"></i></div>
            <p style="color:black;font-size:20px; margin-top:28px">환영합니다. '{{ movie.title }}' 리뷰 채팅방입니다.</p>
            <div style="margin-right:30px"><i class="fa-solid fa-chevron-down fa-2xl" style="color: #363f4f;"></i></div>
        </div>
        <!-- 리뷰 -->
        <div class="review-box">
            <div v-for="(review, idx) in reviews" :key="idx">
                
                <div class="review-content">
                    <!-- 유저 프로필 -->
                    <div class="review-user">
                        <router-link :to="{name:'userprofile', params:{userid:review.user}} "><i class="fa-solid fa-user-astronaut fa-2xl" style="color: #8edae2;"></i>
                            <div style="height: 15px;"></div>
                        <span style="font-weight: 700;">{{ review.nickname }}</span></router-link>
                    </div>
                    <!-- 리뷰 말풍선 -->
                    <div class="speech-bubble">
                        <!-- 별점 -->
                        <div class='RatingStar'>
                            <div class='RatingScore'>
                                <div class='outer-star'><div class='inner-star' :style="{ width: `${review.rate * 20}%` }"></div></div>
                            </div>
                        </div>
                        <div class="divider"></div>
                        <p style="text-align:left; margin-left:13px; margin-top:10px; font-weight: 700;">{{ review.content }}</p>
                    </div>
                </div>
            </div>
        </div>
        
        <UpComingMovieReview/>
    </div>
</div>
</template>

<script>
import UpComingMovieReview from '../components/Movie/UpComingMovieReview.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000/api/v1'
const YOUTUBE_KEY = 'AIzaSyBkdQF46yaw0HH0kpENBBanwFI1y1mGnhI'
// const YOUTUBE_KEY = 'AIzaSyArMcs8a_vXyN3DIt4Qn4gC0dQlE1y9noc'
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

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
            console.log(res)
            this.MovieTrailer = res.data.items[0]
            console.log(this.MovieTrailer)
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
    position: absolute;
    transform: translateY(-145%);
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
    margin-top: 80px;
}
.speech-bubble {
    width: 400px;
	position: relative;
	background:#8edae2;
	border-radius: .4em;
    margin-bottom: 30px;
    box-shadow: 1px 1px 10px #3f3f3f, -1px -1px 10px #3f3f3f;
}
.speech-bubble:after {
	content: '';
	position: absolute;
	left: 0;
	top: 50%;
	width: 0;
	height: 0;
	border: 0.875em solid transparent;
	border-right-color: #8edae2;
	border-left: 0;
	border-top: 0;
	margin-top: -0.437em;
	margin-left: -0.875em;
}
.review-box{
    width: 90%;
    margin-right: auto;
    margin-left: auto;
}
.review-rate{
    margin-top: 3px;
    margin-left: 13px;
    margin-bottom: 1px;
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
.divider{
    height: 1.3px;
    border: none;
    background-color: white;
    margin-left: 5px;
    margin-right: 5px;
    margin-bottom: 2px;
}
.RatingStar{
    display: flex;
    margin-left: 13px;
    margin-top: 5px;
    margin-bottom: 3px;
}

.inner-star::before{color: #ffba24;}
.outer-star {position: relative;display: inline-block;color: #7c7c7c;}
.inner-star {position: absolute;left: 0;top: 0;width: 0%;overflow: hidden;white-space: nowrap;}
.outer-star::before, .inner-star::before {content: '\f005 \f005 \f005 \f005 \f005';font-family: 'Font Awesome 5 free';font-weight: 900;}

</style>