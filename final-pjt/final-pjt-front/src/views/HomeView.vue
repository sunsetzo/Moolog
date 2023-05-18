<template>
  <div></div>
</template>

<script>
export default {
  name : 'HomeView',
  created(){
    this.getUser()
  },
  methods:{
    getUser(){
      this.$store.dispatch('getUser')
    },
  }
}
</script>

<style>

</style>