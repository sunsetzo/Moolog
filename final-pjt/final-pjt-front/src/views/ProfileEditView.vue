<template>
  <div>
    <h1>Profile Edit</h1>
    <hr>
    <div class="profile">
      <div>
        <img :src="image" alt="profile imge">
        <input accept="image/*" ref="inputImage" type="file" value="사진 선택" @change="uploadImg">
      </div>
      <div>
        <label for="EditNickname">NickName : </label>
        <input type="text" id="EditNickname" v-model="nickname">

        <!-- 비밀번호 변경 모달 -->
        <button data-bs-toggle="modal" data-bs-target="#exchangePWModal">비밀번호 변경</button>
        <br>
          <div class="modal fade" id="exchangePWModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exchangePWModal">비밀번호 변경</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <label for="oldpassword"> 기존 비밀번호 : </label>
                  <input type="text" id="oldpassword" v-model="oldpassword">
                  <br>
                  <label for="newpassword1">새로운 비밀번호 : </label>
                  <input type="password" id="newpassword1" v-model="newpassword1">
                  <br>
                  <label for="newpassword2">비밀번호 확인 : </label>
                  <input type="password" id="newpassword2" v-model="newpassword2">
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  <button type="button" class="btn btn-primary" data-bs-dismiss="modal">완료</button>
                </div>
              </div>
            </div>
          </div>
        <!-- 비밀번호 변경 끝 -->
        <button @click="editProfile(nickname, image)">프로필 수정</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name : 'ProfileEditView',
  data(){
    return{
      nickname:null,
      oldpassword : null,
      newpassword1 : null,
      newpassword2 : null,
      image : 'https://www.ncenet.com/wp-content/uploads/2020/04/no-image-png-2.png'
    }
  },
  created(){
    this.getUser()

    this.nickname = this.$store.state.user.nickname
    const oldProfileImg = this.$store.state.user.user_image
    if (oldProfileImg){
      this.image = oldProfileImg
    }
  },  
  methods:{
    getUser(){
      this.$store.dispatch('getUser')
    },
    uploadImg(){
      const image = this.$refs['inputImage'].files[0]
      console.log(image)
      const imageURL = URL.createObjectURL(image)
      console.log(imageURL)
      this.image = imageURL
    },
    editProfile(nickname, user_image){
      const token = this.$store.state.login.token
      const payload = { nickname, user_image, token }
      console.log(payload)
      this.$store.dispatch('editProfile', payload)
    }
  }
}
</script>

<style>
.profile {
  display: flex;
}
</style>