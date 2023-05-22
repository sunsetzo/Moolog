<template>
  <div>
    <div class="modal fade" id="randomMovieModal" tabindex="-1" aria-labelledby="randomMovieModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="randomMovieModalLabel">오늘의 랜덤 영화</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                추천 영화
                <br>
                <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${randomMovie[0].poster_path}`" alt="">
                <br>
                {{ randomMovie[0].title }}
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
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

<style>

</style>