<template>
  <div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name : 'MovieList',
  components:{
  },
  computed:{
    ...mapGetters(['Movies']),
  },
}
</script>

<style>

</style>