<template>
  <div>
    <input
    type="text" v-model="searchInput" 
    placeholder="영화 제목을 입력하세요."
    @keyup.enter="searchMovie">
    <v-btn outlined @click="searchMovie">검색</v-btn>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name : 'SearchBar',
  data(){
    return{
      searchInput : null,
      searchResult : []
    }
  },
  computed:{
    ...mapGetters(['Movies' ])
  },
  methods:{
    searchMovie(){
      this.searchResult = []

      this.Movies.forEach((movie) => {
        if (movie.title.includes(this.searchInput)) {
          this.searchResult.push(movie)
        }
      })


      this.$router.push({name:'search', query: { searchResult: this.searchResult, searchInput: this.searchInput }})
      
      this.searchInput = ''
    }
  }
}
</script>

<style>

</style>