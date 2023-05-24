<template>
  <div class="d-flex align-items-center justify-content-center">
    <input
    type="text" v-model="searchInput"
    class="me-1"
    style="color: white; width:500px; height: 50px; border: 1px solid white;
          border-radius: 30px; margin-top:10px; margin-bottom: 10px; text-align: center;"
    placeholder="영화 제목을 입력하세요."
    @keyup.enter="searchMovie">
    <v-btn color="white search-icon" dark style="background-color:black;" @click="searchMovie">
      <v-icon dark>fas fa-search</v-icon>
    </v-btn>
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

<style scoped>
.search-icon {
  
}
</style>