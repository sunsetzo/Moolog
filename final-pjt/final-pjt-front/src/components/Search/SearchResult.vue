<template>
  <div>
    <div>
      <input
        type="text" v-model="input" 
        placeholder="영화 제목을 입력하세요."
        @keyup.enter="searchMovie">
      <v-btn outlined @click="searchMovie">검색</v-btn>
    </div>
    <p style="font-size: 30px; font-weight: 500;">{{ searchInput }} 검색한 결과</p>
    <p>{{ searchResultCount }} 개의 검색 결과가 있습니다.</p>
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