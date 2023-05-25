<template>
  <div>
    <div v-show="isRecommend">
        <div class="d-flex ms-2 text-color section-title" style="color: #4DD0E1;">
            <span>Reco</span>
            <span>mmend</span>
            <span class="ms-1">Mo</span>
            <span>vies</span>
        </div>
        <v-main class="main-container">
            <v-carousel
            class="carousel-container"
            hide-delimiters>
            <template v-for="(item, index) in recommendMovie">
                <v-carousel-item
                v-if="(index + 1) % columns === 1 || columns === 1"
                :key="index"
                @mouseenter="showInfo(index)"
                @mouseleave="hideInfo(index)"
                >
                <v-row class="flex-nowrap" style="height: 100%">
                    <template v-for="(n, i) in columns">
                    <v-col :key="i">
                        <v-sheet
                        v-if="(+index + i) < recommendMovie.length"
                        >
                        <v-row class="fill-height" align="center" justify="center">
                            <div class="position-relative">
                                <v-img
                                :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${recommendMovie[+index + i].poster_path}`"
                                :alt="recommendMovie[+index + i].title"
                                height="100%"
                                class="imgJanela hoverIMG"
                                ></v-img>
                                <div class="position-absolute top-50 start-50 translate-middle w-100" v-show="visibleIndex === index">
                                <div>
                                    <p style="color:white;">{{ recommendMovie[+index + i].title }}</p>
                                    <div>
                                    <i class="fa-solid fa-star mb-3" style="color: #ff6a38;"><span>   {{ recommendMovie[+index + i].vote_avg }}</span></i>
                                    </div>
                                </div>
                                <div>
                                    <router-link :to="{name:'moviedetail', params:{id:recommendMovie[+index + i].id}}">
                                    <v-btn outlined large elevation="7" color="#FFFFFF">
                                        <span class="me-1">상세보기</span>
                                        <v-icon small>fas fa-search</v-icon>
                                    </v-btn>
                                    </router-link>
                                </div>
                                </div>
                            </div>
                        </v-row>
                        </v-sheet>
                    </v-col>
                    </template>
                </v-row>
                </v-carousel-item>
            </template>
            </v-carousel>
        </v-main>
    </div>
    <div v-show="!isRecommend">
        <div class="mt-3 mb-3 mx-auto" style="color:whitesmoke; width:700px;">
            <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
            <symbol id="check-circle-fill" viewBox="0 0 16 16">
                <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
            </symbol>
            <symbol id="info-fill" viewBox="0 0 16 16">
                <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm.93-9.412-1 4.705c-.07.34.029.533.304.533.194 0 .487-.07.686-.246l-.088.416c-.287.346-.92.598-1.465.598-.703 0-1.002-.422-.808-1.319l.738-3.468c.064-.293.006-.399-.287-.47l-.451-.081.082-.381 2.29-.287zM8 5.5a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"/>
            </symbol>
            <symbol id="exclamation-triangle-fill" viewBox="0 0 16 16">
                <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
            </symbol>
            </svg>
            <div class="alert alert-info d-flex align-items-center justify-content-center custom-margin-1" role="alert" style="height:50px;">
            <svg class="bi flex-shrink-0 me-2" role="img" aria-label="Success:" style="width:25px; height:25px;"><use xlink:href="#check-circle-fill"/></svg>
                <div>
                    선호하시는 영화에 좋아요를 누르면 해당 영화와 유사한 장르의 영화가 추천됩니다.
                </div>
            </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import {sampleSize} from 'lodash'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name:'RecommendMovie',
    data(){
        return{
            recommendMovies : [],
            recommendMovie : [],
            isRecommend : false,
            isVisible: false,
            visibleIndex: null,
        }
    },
    created(){
        const token = this.$store.state.login.token
        axios({
            method:'get',
            url : `${API_URL}/api/v1/recommend_movies/`,
            headers:{
                Authorization: `Token ${token}`
            }
        })
        .then((res)=>{
            this.recommendMovies = res.data
            this.recommendMovie = sampleSize(this.recommendMovies, 12)
            if (this.recommendMovies.length > 0){
                this.isRecommend = true
                console.log(this.isRecommend)
            }
        })
        .catch(()=>{
            console.log('recommend err')
        })
    },
    computed:{
        columns() {
            if (this.$vuetify.breakpoint.xl) {
                return 6;
            }

            if (this.$vuetify.breakpoint.lg) {
                return 6;
            }

            if (this.$vuetify.breakpoint.md) {
                return 3;
            }

            return 3;
            }
    },
    methods: {
        showInfo(index) {
           this.visibleIndex = index;
        },
        hideInfo() {
            this.visibleIndex = null;
        },
    },
}
</script>

<style scoped>

.imgJanela:hover {
    transform: scale(1.1);
}
.hoverIMG{
  -webkit-filter: grayscale(0) blur(0);
  filter: grayscale(0) blur(0);
  -webkit-transition: .3s ease-in-out;
  transition: .3s ease-in-out;
}
.hoverIMG:hover{
  -webkit-filter: grayscale(100%) blur(3px);
  filter: grayscale(100%) blur(3px);
}

/* Fonts at: https://www.google.com/fonts */
@import url('https://fonts.googleapis.com/css?family=Pathway+Gothic+One');

.section-title {
  font-family: 'Pathway Gothic One', sans-serif;
  font-size: 35px;
  position: relative;
  letter-spacing: -2px;
  color: #4DD0E1;
}

.section-title span:before {
  content: '';
  height: 1px;
  position: absolute;
  bottom: 7px;
  background: #4DD0E1;
  width: 0%;
  animation: voila 1s forwards linear;
}

.section-title span:nth-child(2) {
  opacity: .75;
}

.section-title span:nth-child(3) {
  opacity: .5;
}

.section-title span:nth-child(4) {
  opacity: .25;
}

@keyframes voila {
  to { width: 100%; }
}
</style>