<template>
  <div>
    <div v-show="isRecommend">
        <v-app  class="app-container">
            <v-main class="main-container">
                <v-carousel
                class="carousel-container"
                hide-delimiters>
                <template v-for="(item, index) in recommendMovie">
                    <v-carousel-item
                    v-if="(index + 1) % columns === 1 || columns === 1"
                    :key="index"
                    >
                    <v-row class="flex-nowrap" style="height: 100%">
                        <template v-for="(n, i) in columns">
                        <v-col :key="i">
                            <v-sheet
                            v-if="(+index + i) < recommendMovie.length"
                            >
                            <v-row class="fill-height" align="center" justify="center">
                                <div class="image-container">
                                    <v-img
                                    :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${recommendMovie[+index + i].poster_path}`"
                                    :alt="recommendMovie[+index + i].title"
                                    height="100%"
                                    class="imgJanela hoverIMG"
                                ></v-img>
                                <div class="image-title">
                                    {{ recommendMovie[+index + i].title }}   
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
        </v-app>
    </div>
    <div v-show="!isRecommend">
        <h3>추천 영화를 받을라믄 영화 좋아요를 눌러주세용~</h3>
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
    }
}
</script>

<style scoped>

</style>