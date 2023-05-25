<!-- 리뷰 작성 폼 -->
<template>
    <div>
        <!-- 내가 쓴 리뷰 바로 띄우기 -->
        <div class="review-box">
            <div v-for="(myReview) in moviereview" :key="myReview.id">
                <div class="review-content">
                    <div class="speech-bubble">
                        <div class='RatingStar'>
                            <div class='RatingScore'>
                                <div class='outer-star'><div class='inner-star' :style="{ width: `${myReview.rate * 20}%` }"></div></div>
                            </div>
                        </div>
                        <div class="divider"></div>
                        <p style="text-align:left; margin-top: 5px; margin-left: 13px;">{{ myReview.content }}</p>
                    </div>
                    <div class="review-user">
                        <router-link :to="{name:'userprofile', params:{userid:myReview.user}} "><i class="fa-brands fa-reddit-alien fa-2xl" style="color: #8edae2;"></i>
                            <div style="height: 10px;"></div>
                        <span>{{ myReview.nickname }}</span></router-link>
                    </div>
                    <!-- 삭제 버튼 -->
                    <i @click="deleteReview(myReview)" class="fa-solid fa-trash-can fa-xl" style="color: #8edae2; align-items: center;
                    margin-top: 30px; margin-left: 15px;"></i>

                </div>
            </div>
        </div>
        <div style="height:1px; width:99%; margin:20px auto 0px; background-color: white;"></div>
        <div style="height: 8px;"></div>
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
        </fieldset>
        <div style="padding-bottom: 50px; padding-top: 5px;">
            <input type="text" v-model="content" style="color: white; border: 1px solid white; border-radius: 5px;
                width: 85%; height: 80px; text-align: left; padding-left: 10px;"
                placeholder="리뷰를 입력해주세요" @keyup.enter="createReview">
            <input type="submit" id="submit" class="btn" value="확인" @click="createReview"
                style="border:1px #8edae2 solid; border-radius: 5px; width:100px; height:80px; margin-left:5px; color:white; background-color: #8edae2;">
        </div>
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
                alert('별점을 입력해주세요')
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
.rate { border: 0; width:86%}
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
	background: #EEEEEE;
	border-radius: .4em;
    color: black;
    margin-left: auto;
    margin-bottom: 30px;
    box-shadow: 1px 1px 10px #3f3f3f, -1px -1px 10px #3f3f3f;
}

.speech-bubble:after {
	content: '';
	position: absolute;
	right: 0;
	top: 50%;
	width: 0;
	height: 0;
	border: 0.875em solid transparent;
	border-left-color: #EEEEEE;
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
    margin-top: 8px;
    margin-left: 10px;
}
.review-user{
    align-self: auto;
    margin-left: 15px;
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
.divider{
    height: 1.3px;
    border: none;
    background-color: #424242;
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
.inner-star::before{color: #FF9600;}
.outer-star {position: relative;display: inline-block;color: #CCCCCC;}
.inner-star {position: absolute;left: 0;top: 0;width: 0%;overflow: hidden;white-space: nowrap;}
.outer-star::before, .inner-star::before {content: '\f005 \f005 \f005 \f005 \f005';font-family: 'Font Awesome 5 free';font-weight: 900;}

 
</style>