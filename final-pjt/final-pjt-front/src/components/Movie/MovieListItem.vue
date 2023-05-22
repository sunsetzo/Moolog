<template>
  <div>
    {{ movie?.title }}
  </div>
</template>

<script>
export default {
  name:'MovieListItem',
  props:{
    movie: Object
  }

}
</script>

<style>

</style>