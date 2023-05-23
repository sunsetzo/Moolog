<!-- 리뷰 작성 폼 -->
<template>
    <div>
        <div v-for="(myReview) in moviereview" :key="myReview.id">
            <p>별점 : {{ myReview.rate }}</p>
            <p>{{ myReview.content }}</p>
            <br>
            <button class="btn" @click="deleteReview(myReview)">삭제</button>
        </div>
        <fieldset class="rate">
            <input type="radio" id="rating10" name="rating" value="10" @change="handleRatingChange"><label for="rating10" title="5점"></label>
            <input type="radio" id="rating9" name="rating" value="9" @change="handleRatingChange"><label class="half" for="rating9" title="4.5점"></label>
            <input type="radio" id="rating8" name="rating" value="8" @change="handleRatingChange"><label for="rating8" title="4점"></label>
            <input type="radio" id="rating7" name="rating" value="7" @change="handleRatingChange"><label class="half" for="rating7" title="3.5점"></label>
            <input type="radio" id="rating6" name="rating" value="6" @change="handleRatingChange"><label for="rating6" title="3점"></label>
            <input type="radio" id="rating5" name="rating" value="5" @change="handleRatingChange"><label class="half" for="rating5" title="2.5점"></label>
            <input type="radio" id="rating4" name="rating" value="4" @change="handleRatingChange"><label for="rating4" title="2점"></label>
            <input type="radio" id="rating3" name="rating" value="3" @change="handleRatingChange"><label class="half" for="rating3" title="1.5점"></label>
            <input type="radio" id="rating2" name="rating" value="2" @change="handleRatingChange"><label for="rating2" title="1점"></label>
            <input type="radio" id="rating1" name="rating" value="1" @change="handleRatingChange"><label class="half" for="rating1" title="0.5점"></label>
            <br>
            <hr>  
            <form @submit.prevent="createReview">
                <label for="content">내용 : </label>
                <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
                <input type="submit" id="submit">
            </form>
        </fieldset>
    </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000/api/v1'

export default {
    name : 'UpComingMovieReview',
    components:{
    },
    props:{
    },
    data(){
        return{
            moviereview : [],
            content : '',
            selectedRatingCount: 0
        }
    },
    created(){
        this.content = ''
    },
    methods:{
        handleRatingChange() {
            const selectedRating = document.querySelector('input[name="rating"]:checked');
            if (selectedRating) {
                this.selectedRatingCount = selectedRating.value;
            } else {
                this.selectedRatingCount = 0;
            }
        },
        createReview(){
            const content = this.content
            const rate = this.selectedRatingCount / 2
            const token = this.$store.state.login.token

            if (!content){
                alert('리뷰를 입력해주세요')
                return
            }else if(rate===0){
                alert('별점 0점이 맞나요 닝겐')
                return
            }
            axios({
                method:'post',
                url:`${API_URL}/upcoming_movies/${this.$route.params.id}/reviews/`,
                data:{content, rate},
                headers:{
                    Authorization: `Token ${token}`
                }
            })
            .then((res)=>{
                console.log(res)
                this.moviereview.push(res.data)
                this.content = null
                const radioButtons = document.getElementsByName('rating');
                radioButtons.forEach(button => {
                    button.checked = false;
                })
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        deleteReview(review){
            const token = this.$store.state.login.token
            axios({
                method:'delete',
                url:`${API_URL}/upcoming_movies/reviews/${review.id}`,
                headers:{
                    Authorization: `Token ${token}`
                }
            })
            .then((res)=>{
                console.log(res)
                this.moviereview.splice(res.data.id, 1)
            })
            .catch((err)=>{
                console.log(err)
            })
        },
    }
}
</script>

<style scoped>
/* @import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css); */
.rate { display: inline-block;border: 0;margin-right: 15px;}
.rate > input {display: none;}
.rate > label {float: right;color: #ddd}
.rate > label:before {display: inline-block;font-size: 1rem;padding: .3rem .2rem;margin: 0;cursor: pointer;font-family: FontAwesome;content: "\f005 ";}
.rate .half:before {content: "\f089 "; position: absolute;padding-right: 0;}
.rate input:checked ~ label, 
.rate label:hover,.rate label:hover ~ label { color: #f73c32 !important;  } 
.rate input:checked + .rate label:hover,
.rate input input:checked ~ label:hover,
.rate input:checked ~ .rate label:hover ~ label,  
.rate label:hover ~ input:checked ~ label { color: #f73c32 !important;  } 
</style>