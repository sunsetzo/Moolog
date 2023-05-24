<template>
  <div>
    <div class="d-flex align-items-center justify-content-center">
      <input
        type="text" v-model="input"
        class="me-1"
        style="color: white; width:500px; height: 50px; border: 1px solid white;
              border-radius: 30px; margin-top:10px; margin-bottom: 10px;  text-align: center;"
        placeholder="영화 제목을 입력하세요."
        @keyup.enter="searchMovie">
      <v-btn color="white" dark style="background-color:black;" @click="searchMovie">
        <v-icon dark>fas fa-search</v-icon>
      </v-btn>
    </div>
    <p style="font-size: 30px; font-weight: 500; color:whitesmoke;">{{ searchInput }} 검색한 결과</p>
    <p style="color:whitesmoke;">{{ searchResultCount }} 개의 검색 결과가 있습니다.</p>
    <div class="row row-cols-1 row-cols-md-6 g-2 mx-auto" :class="{ 'justify-content-center': searchResult.length < 6 }">
      <SearchResultItem v-for="movie in searchResult" :key="movie.id" :movie="movie"/>
    </div>
  </div>
</template>

<script>
import SearchResultItem from './SearchResultItem.vue';

import { mapGetters } from 'vuex';


export default {
  name : 'SearchResult',
  components:{
    SearchResultItem,
  },
  data () {
    return {
      input: null,
      result : [],
      searchResult: this.$route.query.searchResult,
    }
  },
  computed : {
    ...mapGetters(['Movies']),
    searchInput() {
      return this.$route.query.searchInput || ''
    },
    searchResultCount() {
      return this.$route.query.searchResult.length
    }
  },
  methods : {
    searchMovie(){
      this.result = []
      
      if (this.input.trim()) {
        
        if (this.input === this.searchInput) {
          alert("현재 검색된 결과입니다.")
          return
        }
        this.Movies.forEach((movie) => {
          if (movie.title.includes(this.input)) {
            this.result.push(movie)
          }
        })

        this.searchResult = [] // 기존 검색 결과 초기화
  
        this.result.forEach((movie) => {
          this.searchResult.push(movie)
        })
  
        this.$router.replace({
          name:'search', 
          query: { searchResult: this.result, searchInput: this.input,
        }})
        
        this.input = ''
      } else {
        alert('검색어를 입력해주세요.')
      }

    }
  },
}
</script>

<style scoped>
.row-cols-1 {
  justify-content: flex-start;
}

.justify-content-center {
  justify-content: center;
}
</style>