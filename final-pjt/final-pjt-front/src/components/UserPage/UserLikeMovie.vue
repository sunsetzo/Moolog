<template>
    <div>
        <p>유저가 좋아요 한 영화</p>
        <v-app class="app-container">
            <v-main class="main-container">
                <v-carousel
                class="carousel-container"
                hide-delimiters>
                <template v-for="(item, index) in userLikeMovies">
                    <v-carousel-item
                    v-if="(index + 1) % columns === 1 || columns === 1"
                    :key="index"
                    >
                    <v-row class="flex-nowrap" style="height: 100%">
                        <template v-for="(n, i) in columns">
                        <v-col :key="i">
                            <v-sheet
                            v-if="(+index + i) < userLikeMovies.length"
                            >
                            <v-row class="fill-height" align="center" justify="center">
                                
                                <div class="image-container">
                                <v-img
                                    :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${userLikeMovies[+index + i].poster_path}`"
                                    :alt="userLikeMovies[+index + i].title"
                                    height="100%" 
                                    class="imgJanela hoverIMG"
                                ></v-img>
                                <div class="image-title">
                                    {{ userLikeMovies[+index + i].title }}
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
  </template>
  
  <script>
import { mapGetters } from 'vuex'
  export default {
      name:'UserLikeMovie',
      data(){
        return{
            userLikeMovies : []
        }
      },
      computed:{
        ...mapGetters(['userprofile']),
        columns() {
            if (this.$vuetify.breakpoint.xl) {
                return 6;
            }

            if (this.$vuetify.breakpoint.lg) {
                return 4;
            }

            if (this.$vuetify.breakpoint.md) {
                return 3;
            }

            return 1;
            }
      },
      created(){
        this.userprofile.like_now_playing_movies.forEach((el)=>{
        this.userLikeMovies.push(el)
        })
        this.userprofile.like_upcoming_movies.forEach((el)=>{
        this.userLikeMovies.push(el)
        })
        this.userprofile.like_popular_movies.forEach((el)=>{
        this.userLikeMovies.push(el)
        })
        console.log(this.userLikeMovies)
      }
  }
  </script>
  
  <style>
  
  </style>