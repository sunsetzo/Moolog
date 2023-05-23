<template>
  <div>
    <!-- <v-app> -->
      <v-dialog v-model="modalOpen" max-width="500px" eager>
        <template v-slot:activator="{ on }">
          <img class="logo" src="@/assets/moolog_nobg.png" alt="logo" v-on="on">
        </template>
        <v-card>
          <div :style="headerStyle" class="d-flex">
            <v-toolbar class="text-h6" color="#00ACC1" dark dense>
              <v-toolbar-title>오늘의 랜덤 영화</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-card-actions>
                <v-btn color="white" text @click="closeModal" style="min-width: 10px; position: relative; left: 15px;">x</v-btn>
              </v-card-actions>
            </v-toolbar>
          </div>
          <v-card-text>
            <div class="text-center">
              추천 영화
              <br />
              <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${randomMovie[0].poster_path}`" alt="" />
              <br />
              {{ randomMovie[0].title }}
            </div>
          </v-card-text>
          <v-card-actions class="d-flex justify-content-center">
            <v-btn color="#00ACC1" style="color:white;" @click="getRandomMovie">Random!</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    <!-- </v-app> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name:'RandomMovie',
  computed:{
      ...mapGetters(['randomMovie'])
  },
  data() {
      return {
          modalOpen: false,
          headerStyle: "",
      }
  },
  created(){
      this.getRandomMovie()
  },
  methods:{
      getRandomMovie(){
          this.$store.commit('getRandomMovie')
      },
      openModal() {
      // 모달이 열릴 때 header 크기를 설정
      this.headerStyle = "height: 64px"; // 예시로 64px로 설정, 실제 값에 맞게 수정
      this.modalOpen = true
      },
      closeModal() {
      // 모달이 닫힐 때 header 크기를 복원
      this.headerStyle = ""; // 원래의 header 스타일로 복원
      this.modalOpen = false;
      },
  },
}
</script>

<style scoped>
.logo{
  margin: 30px;
  width: 250px;
}
</style>