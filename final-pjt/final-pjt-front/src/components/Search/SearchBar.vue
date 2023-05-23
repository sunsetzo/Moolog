<template>
  <div>
    <input 
    type="text" v-model="searchInput" 
    placeholder="영화 제목을 입력하세요"
    @input="searchMovie">
    <button @click="searchMovie">검색</button>
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
    ...mapGetters(['allMovies' ])
  },
  methods:{
    searchMovie(){
      if (this.allMovies.includes(this.searchInput)){
        this.searchResult.push(this.allMovies)
      }
      this.$router.push({name:'search'})
      
      // this.allMovies.forEach((el)=>{
      //   if (el.includes(this.searchInput)){
      //     this.searchResult.push(el)
      //   }
      // })
    }
  }
}
</script>

<style>

</style>