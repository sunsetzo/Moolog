<template>
  <div>
    <div class="row row-cols-1 row-cols-md-6 g-2 mx-auto">
        <MovieListItem v-for="(movie) in movies" :key="movie.id" :movie="movie"
        class="col"
        />
        <infinite-loading v-if="hasMore" @infinite="infiniteHandler" spinner="waveDots"></infinite-loading>
    </div>  
  </div>
</template>

<script>
import axios from 'axios'
import InfiniteLoading from 'vue-infinite-loading';
import { mapGetters } from 'vuex';
import MovieListItem from './MovieListItem.vue';


const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'MovieList',
  components:{
    MovieListItem,
    InfiniteLoading,
  },
  data() {
    return {
      page: 0,
      movies: [],
    }
  },
  computed:{
    ...mapGetters(['Movies']),
    hasMore() {
      return  this.movies.length < this.Movies.length && this.Movies.length > 0
    },
  },
  methods:{
    getMovie(){
      this.$store.dispatch('getMovies')
    },
    infiniteHandler($state) {
      axios({
        method: 'get',
        url:`${API_URL}/api/v1/popular_movies/scroll/${this.page}/`,
      })
      .then((res) => {
        setTimeout(() => {
          if (res.data.length) {
          console.log(res.data)
          this.movies = [...this.movies, ...res.data]
          this.page += 1
          $state.loaded()
        } else {
          $state.complete()
        }
        }, 700)
        
      })
      .catch((err) => {
        console.log(err)
        $state.complete()
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

</style>