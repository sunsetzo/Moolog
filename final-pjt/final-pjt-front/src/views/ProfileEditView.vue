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
        <br>
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
                  <input type="password" id="oldpassword" v-model="oldpassword">
                  <br>
                  <label for="newpassword1">새로운 비밀번호 : </label>
                  <input type="password" id="newpassword1" v-model="newpassword1">
                  <br>
                  <label for="newpassword2">비밀번호 확인 : </label>
                  <input type="password" id="newpassword2" v-model="newpassword2" @keyup="checkPW">
                  <p>{{ message }}</p>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                  <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="completePW">완료</button>
                </div>
              </div>
            </div>
          </div>
        <!-- 비밀번호 변경 끝 -->
        <button @click="editProfile(nickname)">프로필 수정</button>
        <button @click="signOut">회원탈퇴</button>
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
      image : '',
      token : this.$store.state.login.token,
      message : ''
    }
  },
  created(){
    this.getUser()

    this.nickname = this.$store.state.user.nickname
    const oldProfileImg = this.$store.state.user.user_image
    if (oldProfileImg){
      this.image = oldProfileImg
    }
    // console.log(oldProfileImg)
  },  
  methods:{
    getUser(){
      this.$store.dispatch('getUser')
    },
    uploadImg(){
      const image = this.$refs['inputImage'].files[0]
      const imageURL = URL.createObjectURL(image)
      this.image = imageURL
      const token = this.token

      this.$store.dispatch('uploadImg', {image, token})
    },
    editProfile(nickname){
      const token = this.token
      const payload = { nickname,  token }
      // console.log(payload)
      this.$store.dispatch('editProfile', payload)
      this.$emit('editProfile', nickname)
    },
    checkPW(){
      if (this.newpassword1!=this.newpassword2 || this.newpassword2!=this.newpassword1){
        this.message = '비밀번호가 일치하지 않습니다'
      }else{
        this.message = ''
      }
    },
    completePW(){
      const oldpassword = this.oldpassword
      const password = this.newpassword1
      const token = this.token
      const payloadPW = { oldpassword, password, token }
      this.$store.dispatch('completePW', payloadPW)
      this.oldpassword = ''
      this.newpassword1 = ''
      this.newpassword2 = ''
    },
    signOut(){
      const userinfo = this.$store.state.user
      this.$store.dispatch('signOut', userinfo)
    }
  }
}
</script>

<style>
.profile {
  display: flex;
}
</style>