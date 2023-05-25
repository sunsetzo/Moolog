<template>
  <div>
    <div v-show="isRecommend">
        <h3 style="color:white;">추천 영화</h3>
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
        <h3>선호하시는 영화에 좋아요를 누르면 해당 영화와 유사한 장르의 영화가 추천됩니다.</h3>
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

            return 1;
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
</style>