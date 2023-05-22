<template>
    <div>
        {{ moviereview }}
    </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000/api/v1'

export default {
    name : 'CurrentMovieReview',
    components:{
    },
    data(){
        return{
            moviereview : [],
        }
    },
    created(){
        this.getMovieDetail()
    },
    methods:{
        getMovieDetail(){
            axios({
                methods:'get',
                url:`${API_URL}/now_playing_movies/${this.$route.params.id}/reviews/`,
            })
            .then((res)=>{
                // console.log(res)
                this.moviereview = res.data
            })
            .catch((err)=>{
                console.log('getMovieReview err', err)
            })
        }
    }
}
</script>

<style>

</style>