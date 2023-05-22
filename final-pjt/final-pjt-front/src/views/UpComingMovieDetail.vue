<template>
    <div>
    <h1>{{movie.title}}</h1>
      <!-- 영화 포스터 및 타이틀 -->
      <div>
      <div>
          <img src="" alt="포스터 이미지">
      </div>
      <div>
          <div>
          <p>별점?</p>
          </div>
          <div>
          영화 상세 정보
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
                url:`${API_URL}/upcoming_movies/${this.$route.params.id}`
            })
            .then((res)=>{
                console.log(res)
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