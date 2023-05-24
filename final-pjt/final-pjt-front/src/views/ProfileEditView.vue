<template>
  <div class="row">
    <h2 style="color: whitesmoke;">회원 정보 수정</h2>
    <div class="astrodivider">
      <div class="astrodividermask"></div>
    </div>

    <div class="col-4">
      <div class="user-image">
        <img :src="image" alt="profile imge">
        <input accept="image/*" ref="inputImage" type="file" value="사진 선택" @change="uploadImg">
      </div>
    </div>

    <div class="col-8">
      <div>
      <label for="EditNickname" style="color: whitesmoke;">NickName : </label>
      <input type="text" id="EditNickname" v-model="nickname" style="color: whitesmoke;">
      <br>
      <!-- 비밀번호 변경 모달 -->
      <button data-bs-toggle="modal" data-bs-target="#exchangePWModal" style="color: whitesmoke;">비밀번호 변경</button>
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
        <button @click="editProfile(nickname)" style="color: whitesmoke;">프로필 수정</button>
        <br>
        <button @click="signOut" style="color: whitesmoke;">회원탈퇴</button>
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
    }else{
      this.image = 'http://127.0.0.1:8000/media/profile_images/user_img.png'
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

<style scoped>
.astrodivider {
  margin:auto;
  width:100%; 
  max-width: 100%;
  position:relative;
}

.astrodividermask { 
    overflow:hidden; height:20px; 
}

.astrodividermask:after { 
      content:''; 
      display:block; margin:-25px auto 0;
      width:100%; height:25px;  
        border-radius:125px / 12px;
       box-shadow:0 0 8px #4DD0E1;
}

.astrodivider i {
    position:absolute;
    top:4px; bottom:4px;
    left:4px; right:4px;
    border-radius:100%;
    border:1px dashed #68beaa;
    text-align:center;
    line-height:40px;
    font-style:normal;
     color:#4DD0E1;
}

.user-image img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
</style>