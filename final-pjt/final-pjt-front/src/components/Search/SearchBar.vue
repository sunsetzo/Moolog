<template>
  <div>
    <input type="text" v-model="searchData" placeholder="영화 제목을 검색하세요">
  </div>
</template>

<script>
export default {
  name : 'SearchBar',
  data(){
    return{
      searchData : null,
    }
  }
}
</script>

<style>

</style>