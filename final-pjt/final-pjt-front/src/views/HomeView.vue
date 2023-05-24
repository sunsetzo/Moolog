<template>
  <div>
    <LogInOO v-show="isLogin"/>
    <LogInXX v-show="!isLogin"/>
  </div>
</template>

<script>
import LogInOO from '@/components/MyPage/LogInOO.vue';
import LogInXX from '@/components/MyPage/LogInXX.vue';
import { mapGetters } from 'vuex';
export default {
  name : 'HomeView',
  components:{
    LogInOO,
    LogInXX
  },
  created(){
    this.getUser()
  },
  methods:{
    getUser(){
      this.$store.dispatch('getUser')
    },
  },
  computed : {
    ... mapGetters(['currentUser', 'isLogin']),
    
}
}
</script>

<style scoped>

</style>