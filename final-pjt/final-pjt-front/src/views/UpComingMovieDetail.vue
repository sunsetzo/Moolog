<template>
    <div>
    <h1>{{movie.title}}</h1>
      <!-- 영화 포스터 및 타이틀 -->
      <div>
      <div>
        <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie?.poster_path}`" alt="포스터 이미지">
      </div>
      <div>
          <div>
            줄거리 : {{ movie?.overview }}
          </div>
      </div>
      </div>
      <!-- 영화 예고편 영상 -->
      <div>
      영화 예고편 유튜브 api
      </div>
      <!-- 영화 리뷰 -->
      <div>
        <p v-for="review in reviews" :key="review.id">{{ review.content }}</p>
        <UpComingMovieReview/>
      </div>
    </div>
</template>

<script>
import UpComingMovieReview from '../components/Movie/UpComingMovieReview.vue'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000/api/v1'

export default {
    name:'UpComingMovieDetail',
    components:{
        UpComingMovieReview
    },
    data(){
        return{
            movie : [],
            reviews:[]
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
                console.log(res)
                this.reviews = res.data.upcomingreview_set
                this.movie = res.data
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