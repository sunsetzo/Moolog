<template>
  <div>
    <div class="row row-cols-1 row-cols-md-6 g-2 mx-auto">
        <MovieListItem v-for="(movie) in Movies" :key="movie.id" :movie="movie"
        class="col"
        />
        <infinite-loading @infinite="infiniteHandler"></infinite-loading>
    </div>  
  </div>
</template>

<script>
import axios from 'axios'
import InfiniteLoading from 'vue-infinite-loading';
import { mapGetters } from 'vuex';
import MovieListItem from './MovieListItem.vue';

const api = '//hn.algolia.com/api/v1/search_by_date?tags=story'

export default {
  name : 'MovieList',
  components:{
    MovieListItem,
    InfiniteLoading,
  },
  data() {
    return {
      page: this.$route.query.page,
      list: [],
    }
  },
  computed:{
    ...mapGetters(['Movies']),
  },
  created(){
    this.getMovie()
  },
  methods:{
    getMovie(){
      this.$store.dispatch('getMovies')
    },
    infiniteHandler($state) {
      axios.get(api, {
        params: {
          page: this.page,
        },
      })
        .then(({data}) => {
          if (data.hits.length) {
            this.list.push(...data.hits)
            $state.loaded()
          } else {
            $state.complete()
          }
        })
    }
  }
}
</script>

<style scoped>
 .custom-margin {
  margin-right: 200px;
  margin-left: 200px;
 }

</style>