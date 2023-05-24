<template>
    <div class="radom">
      <div class="modal fade" id="randomMovieModal" tabindex="-1" aria-labelledby="randomMovieModalLabel" aria-hidden="true">
          <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header" style="background-color: #00ACC1; color:white; height:3.5rem">
                    <v-toolbar-title class="modal-title" style="font-size:large; font-weight:bold">오늘의 랜덤 영화</v-toolbar-title>
                    <button type="button" class="btn btn-custom-close" data-bs-dismiss="modal" aria-label="Close" style="position: relative; left: 12px;"><i class="fa-solid fa-xmark fa-lg"></i></button>
                </div>
                <div class="modal-body">
                    <div class="movie-poster-container" style="position: relative;">
                        <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${randomMovie[0].poster_path}`" alt="poster" style="border-radius:5px;">
                        <div class="movie-title-overlay">{{ randomMovie[0]?.overview | limitText(450) }}</div>
                    </div>
                    <div class="movie-title">
                        {{ randomMovie[0]?.title }}
                    </div>
                    <v-btn color="#00ACC1" style="color:white;" @click="getRandomMovie">RanDom</v-btn>
                </div>
              </div>
          </div>
      </div>
    </div>
</template>
  

<script>
import { mapGetters } from 'vuex'

export default {
    name:'RandomMovie',
    computed:{
        ...mapGetters(['randomMovie'])
    },
    filters: {
        limitText(text, limit) {
        if (text && text.length > limit) {
            return text.slice(0, limit) + '...'
        }
        return text
        }
    },
    created(){
        this.getRandomMovie()
    },
    methods:{
        getRandomMovie(){
            this.$store.commit('getRandomMovie')
        }
    }

}
</script>

<style scoped>
.random {
  color: #424242;
}
.btn-custom-close {
  color: white;
  font-size: 1rem;
  opacity: 1;
  transition: opacity 0.3s ease-in-out;
}

.btn-custom-close:hover {
  opacity: 0.8;
}

.movie-poster-container {
  position: relative;
}

.movie-title-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  height: 450px;
  width: 300px;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 5px;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;

  font-size:13px;
  font-style: italic;
  padding-left: 5px;
  padding-right: 5px;
}

.movie-poster-container:hover .movie-title-overlay {
  opacity: 1;
}

.movie-title {
    font-size: 18px;
    font-weight: 800;
    margin-top: 8px;
    margin-bottom: 8px;
}
</style>