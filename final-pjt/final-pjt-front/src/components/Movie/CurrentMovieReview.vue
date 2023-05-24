<!-- 리뷰 작성 폼 -->
<template>
    <div>
        <!-- 내가 쓴 리뷰 바로 띄우기 -->
        <div class="review-box">
            <div v-for="(myReview) in moviereview" :key="myReview.id">
                <div class="star-ratings review-rate">
                    <div 
                    class="star-ratings-fill space-x-2 text-lg"
                    :style="{ width: `${myReview.rate * 20}%` }"
                    >
                        <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
                    </div>
                    <div class="star-ratings-base space-x-2 text-lg">
                        <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
                    </div>
                </div>
                <div class="review-content">
                    <div class="speech-bubble">{{ myReview.content }}</div>
                    <div class="review-user">
                        <router-link :to="{name:'userprofile', params:{userid:myReview.user}} "><i class="fa-solid fa-circle-user fa-2xl" style="color: #00a1b0"></i>
                            <br><br>
                        <span>{{ myReview.nickname }}</span></router-link>
                        <br>
                        <button class="btn" @click="deleteReview(myReview)"
                        style="border:1px white solid; border-radius: 5px; height:30px; margin-left:5px; color:white">삭제</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- 리뷰 작성 -->
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
                <label for="content"></label>
                <input id="content" cols="30" rows="10" v-model="content"
                    style="color: white; width:500px; height: 50px; border: 1px solid white;
                    border-radius: 5px; margin-top:10px; margin-bottom: 10px; text-align: center;"
                    placeholder="리뷰를 입력하세요">
                <input type="submit" id="submit" class="btn" value="확인"
                style="border:1px white solid; border-radius: 5px; height:50px; margin-left:5px; color:white">
            </form>
        </fieldset>
    </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000/api/v1'

export default {
    name : 'CurrentMovieReview',
    components:{
    },
    props:{
    },
    data(){
        return{
            moviereview : [],
            content : '',
            selectedRatingCount: 0,
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
                url:`${API_URL}/now_playing_movies/${this.$route.params.id}/reviews/`,
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
                url:`${API_URL}/now_playing_movies/reviews/${review.id}`,
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


.speech-bubble {
    width: 400px;
	position: relative;
	background: #ffffff;
	border-radius: .4em;
    color: black;
    margin-left: auto;
}

.speech-bubble:after {
	content: '';
	position: absolute;
	right: 0;
	top: 50%;
	width: 0;
	height: 0;
	border: 0.875em solid transparent;
	border-left-color: #ffffff;
	border-right: 0;
	border-top: 0;
	margin-top: -0.437em;
	margin-right: -0.875em;
    margin-left: auto;
}
.review-box{
    width: 80%;
    margin-right: auto;
    margin-left: auto;
}
.review-rate{
    width: 80%;
    margin-top: 30px;
    margin-right: 500px;
    margin-bottom: 5px;
}
.review-user{
    align-self: auto;
    margin-left: 20px;
}
.review-content{
    display: flex;
    justify-content: last baseline;
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
/* .review-container{
    margin-left: auto;
} */
</style>