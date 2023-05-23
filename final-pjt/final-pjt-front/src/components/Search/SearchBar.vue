<template>
  <div class="d-flex align-items-center justify-content-center">
    <input
    type="text" v-model="searchInput" style="color:white; height:32px;"
    class="me-2 ps-2"
    placeholder="영화 제목을 입력하세요."
    @keyup.enter="searchMovie">
    <v-btn outlined style="color:white;" @click="searchMovie">검색</v-btn>
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

      if (this.searchInput.trim()) {
        
        this.Movies.forEach((movie) => {
          if (movie.title.includes(this.searchInput)) {
            this.searchResult.push(movie)
          }
        })
  
        this.$router.push({name:'search', query: { searchResult: this.searchResult, searchInput: this.searchInput }})
        
        this.searchInput = ''
      } else {
        alert('검색어를 입력해주세요.')
      }
    }
  }
}
</script>

<style>

</style>