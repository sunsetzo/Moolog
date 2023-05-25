<template>
  <div>
    <div class="row row-cols-1 row-cols-md-6 g-2 mx-auto">
        <MovieListItem v-for="(movie) in movies" :key="movie.id" :movie="movie"
        class="col"/>
    </div>  
    <div v-infinite-scroll="loadMore" infinite-scroll-disabled="loading" infinite-scroll-distance="10">
      <div v-if="loading">
        <b-spinner class="mt-5" style="width: 3rem; height: 3rem;" label="Large Spinner" variant="info"></b-spinner>
      </div>
      <div v-if="completed" class="mt-3 mb-3" style="color:whitesmoke;">
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
            영화 조회가 완료되었습니다.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import InfiniteScroll from 'vue-infinite-scroll';
import { mapGetters } from 'vuex';
import MovieListItem from './MovieListItem.vue';


const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'MovieList',
  components:{
    MovieListItem,
  },
  data() {
    return {
      page: 0,
      movies: [],
      loading: false,
      completed: false,
    }
  },
  directives: {
    InfiniteScroll,
  },
  computed:{
    ...mapGetters(['Movies']),
  },
  methods:{
    getMovie(){
      this.$store.dispatch('getMovies')
    },
    loadMore() {
      if (this.loading) return;
      
      if (this.movies.length === this.Movies.length) {
        this.completed = true
        return
      }

      this.loading = true

      axios({
        method: 'get',
        url:`${API_URL}/api/v1/popular_movies/scroll/${this.page}/`,
      })
      .then((res) => {
        setTimeout(() => {
          if (res.data.length) {
          this.movies = [...this.movies, ...res.data]
          this.page += 1
          this.loading = false
          } 
        }, 700)
        
      })
      .catch((err) => {
        console.log(err)
        this.loading = false
      })
    },
  },
  created() {
    this.getMovie()
  },
}
</script>

<style scoped>
 .custom-margin {
  margin-right: 200px;
  margin-left: 200px;
 }

.custom-margin-1 {
  margin-right: 250px;
  margin-left: 250px;
}
</style>