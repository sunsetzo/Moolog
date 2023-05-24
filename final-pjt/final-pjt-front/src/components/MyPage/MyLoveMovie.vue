<template>
  <div>
    내가 좋아요한 영화
    <v-app class="app-container">
      <v-main class="main-container">
        <v-carousel
        class="carousel-container"
        hide-delimiters>
          <template v-for="(item, index) in myLoveMovie">
            <v-carousel-item
              v-if="(index + 1) % columns === 1 || columns === 1"
              :key="index"
            >
              <v-row class="flex-nowrap" style="height: 100%">
                <template v-for="(n, i) in columns">
                  <v-col :key="i">
                    <v-sheet
                      v-if="(+index + i) < myLoveMovie.length"
                    >
                      <v-row class="fill-height" align="center" justify="center">
                        
                        <div class="image-container">
                          <v-img
                            :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${myLoveMovie[+index + i].poster_path}`"
                            :alt="myLoveMovie[+index + i].title"
                            height="100%" 
                            class="imgJanela hoverIMG"
                          ></v-img>
                          <div class="image-title">
                            {{ myLoveMovie[+index + i].title }}
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
  name : 'MyLoveMovie',
  computed:{
    ...mapGetters(['userInfo']),
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
  data(){
    return{
      myLoveMovie : [],
    }
  },
  created(){
    this.userInfo.like_now_playing_movies.forEach((el)=>{
      this.myLoveMovie.push(el)
    })
    this.userInfo.like_upcoming_movies.forEach((el)=>{
      this.myLoveMovie.push(el)
    })
    this.userInfo.like_popular_movies.forEach((el)=>{
      this.myLoveMovie.push(el)
    })
    console.log(this.myLoveMovie)
  },
}
</script >

<style scoped>
.app-container {
  height: 600px; /* 원하는 높이로 설정 */
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
