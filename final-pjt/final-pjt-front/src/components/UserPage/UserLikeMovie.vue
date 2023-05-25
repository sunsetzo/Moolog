<template>
    <div>
        <h3 style="margin-top:30px; color:white">User Like Movies</h3>
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
                            style="width: 300px;"
                            v-if="(+index + i) < userLikeMovies.length"
                            >
                            <v-row class="fill-height" align="center" justify="center">
                                
                                <div class="image-container">
                                <v-img
                                    :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${userLikeMovies[+index + i].poster_path}`"
                                    :alt="userLikeMovies[+index + i].title"
                                    height="100%" 
                                ></v-img>
                                <div class="image-title">
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
  
  <style scoped>
  .app-container {
  height: 400px; /* 원하는 높이로 설정 */
}
.main-container {
  height: 100%; /* 부모 요소인 v-app의 높이에 맞춤 */
}
.carousel-container{
  width: 2000px;
  margin: auto;
}
.info-sheet {
  width: 300px;
  height: 400px;
}
  </style>