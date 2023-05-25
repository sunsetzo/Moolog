<template>
  <div>
    <h2 style="color: whitesmoke;">회원 정보</h2>
      <div class="astrodivider">
        <div class="astrodividermask"></div>
      </div>

    <div class="row profile-container">
      <div class="col-4 col-4-container">
        <div class="user-image">
          <img :src="image" alt="profile imge" class="mb-3" v-if="isImage">
          <img src="@/assets/user_img.png" alt="default image" class="mb-3" v-if="!isImage">
          <h5 class="fw-bold">{{ fixedNickname }}</h5>
          <p style="font-size:13px; height:15px;">{{ email }}</p>
          <div class="filebox">
            <input class="upload-name" :value="fileName" placeholder="첨부파일" style="font-size:13px;" disabled>
            <label for="file" style="font-size:13px;">사진 변경</label> 
            <input type="file" id="file" accept="image/*" ref="inputImage" @change="uploadImg" @input="setFileName">
          </div>
        </div>
      </div>

      <div class="col-8">
        <div style="position:relative; top:45px;">
          <div class="basic-info text-start ms-2 me-1">
            <p class="basic-info-title ms-2 mt-2 mb-1">기본 정보<i class="fa-solid fa-circle-info fa-lg ms-1" style="color:#616161; position:relative; bottom:2px;"></i></p>
            <div class="d-flex">
              <label for="nickname" class="form-label margin-custom" style="font-size:13px;">NICKNAME</label>
              <input type="text" class="form-control ms-2 me-2 mb-2" id="nickname" aria-describedby="emailHelp" v-model="nickname" 
              placeholder="NICKNAME" style="font-size:14px;">
              <button @click="editProfile(nickname)" 
              style="background-color:#7E57C2; font-size:14px; color:white; border-radius:3px; width:70px;"
              class="mb-2 me-2"
              >수정</button>
            </div>
          </div>
        
          <div class="basic-info text-start ms-2 me-1 mt-4">
            <p class="basic-info-title ms-2 mt-2 mb-1">보안 정보<i class="fa-solid fa-lock fa-lg ms-1" style="color:#616161; position:relative; bottom:2px"></i></p>
            <p class="ms-2 mb-1" style="font-size:14px;">비밀번호 초기화 이메일<span class="ms-3" style="color:#BDBDBD;">{{ email }}</span></p>
            <a href="#" data-bs-toggle="tooltip" title="비밀번호 변경 창을 띄워줍니다.">
              <button class="ms-2" style="font-size:14px; color:#616161;" data-bs-toggle="modal" data-bs-target="#exchangePWModal">
                <i class="fa-solid fa-chevron-right fa-sm me-1"></i>비밀번호 변경
              </button>
            </a>
          </div>
        <!-- 비밀번호 변경 모달 -->
          <div class="modal fade" id="exchangePWModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header" style="background-color: #7E57C2; color:white; height:3.5rem">
                  <v-toolbar-title class="modal-title" style="font-size:large; font-weight:bold">Password Change</v-toolbar-title>
                  <button type="button" class="btn btn-custom-close" data-bs-dismiss="modal" aria-label="Close" style="position: relative; left: 12px;"><i class="fa-solid fa-xmark fa-lg"></i></button>
                </div>

                <div class="modal-body">
                  <div class="mb-3">
                    <div class="d-flex ms-1">
                      <a href="#" data-bs-toggle="tooltip" title="기존 비밀번호를 입력하세요.">
                        <label for="oldpassword" class="form-label" style="color:black;">PASSWORD</label>
                      </a>
                    </div>
                    <input type="password" class="form-control" id="oldpassword" aria-describedby="emailHelp" v-model="oldpassword">
                  </div>
                  <div class="mb-3">
                    <div class="d-flex ms-1">
                      <a href="#" data-bs-toggle="tooltip" title="새로운 비밀번호를 입력하세요.">
                        <label for="newpassword1" class="form-label" style="color:black;">NEW PASSWORD</label>
                      </a>
                    </div>
                    <input type="password" class="form-control" id="newpassword1" aria-describedby="emailHelp" v-model="newpassword1">
                  </div>
                  <div class="mb-3">
                    <div class="d-flex ms-1">
                      <a href="#" data-bs-toggle="tooltip" title="새로운 비밀번호를 한 번 더 입력하세요.">
                        <label for="newpassword2" class="form-label" style="color:black;">NEW PASSWORD CONFIRMATION</label>
                      </a>
                    </div>
                    <input type="password" class="form-control" id="newpassword2" aria-describedby="emailHelp" v-model="newpassword2" @keyup="checkPW">
                  </div>
                  <p style="font-size:14px; color:red; font-weight:bold;">{{ message }}</p>
                </div>
                <div class="modal-footer">
                  <button class="btn" style="background-color: #7E57C2; color:white;" data-bs-dismiss="modal" @click="completePW">OK</button>
                </div>
              </div>`
            </div>
          </div>
          <!-- 비밀번호 변경 끝 -->

          <div class="d-flex justify-content-end me-2 mt-1">
            <a href="#" data-bs-toggle="tooltip" title="클릭시 회원 탈퇴가 진행됩니다.">
              <button style="font-size:14px; color:#616161;" @click="signOut">
                <i class="fa-solid fa-chevron-right fa-sm me-1"></i>회원 탈퇴
              </button>
            </a>
          </div>
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name : 'ProfileEditView',
  data(){
    return{
      isImage: false,
      fixedNickname: null,
      nickname:null,
      email: null,
      oldpassword : null,
      newpassword1 : null,
      newpassword2 : null,
      image : '',
      token : this.$store.state.login.token,
      message : '',
      fileName: ''
    }
  },
  created(){
    this.getUser()

    this.nickname = this.$store.state.user.nickname
    this.fixedNickname = this.$store.state.user.nickname
    this.email = this.$store.state.user.email
    const oldProfileImg = this.$store.state.user.user_image
    if (oldProfileImg){
      this.image = oldProfileImg
      this.isImage = true
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
    },
    setFileName() {
      const fileInput = this.$refs['inputImage']
      if (fileInput.files.length > 0) {
        this.fileName = fileInput.files[0].name
      } else {
        this.fileName = ''
      }
    },
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
  box-shadow:0 0 8px #7E57C2;
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
  color:#7E57C2;
}

.user-image img {
  width: 200px;
  height: 200px;
  border-radius: 50%;
}

.profile-container {
  background: white;
  border-radius: 5px;
  margin-left: 5px;
  margin-right: 5px;
}

.col-4-container{
  box-shadow: 0.2px 0px 10px 1px rgba(74, 74, 74, 0.736);
}

.col-8-container{
 background-color: #F5F5F5;
}

.filebox .upload-name {
    display: inline-block;
    height: 30px;
    padding: 0 10px;
    vertical-align: middle;
    border: 1px solid #dddddd;
    border-radius: 3px;
    width: 50%;
    color: #999999;
}

.filebox label {
    display: inline-block;
    padding: 5px 10px;
    color: #fff;
    vertical-align: middle;
    background-color: #7E57C2;
    cursor: pointer;
    height: 30px;
    margin-left: 10px;

    border-radius: 3px;
}

.filebox input[type="file"] {
    position: absolute;
    width: 0;
    height: 0;
    padding: 0;
    overflow: hidden;
    border: 0;
}

.margin-custom {
  margin: 8px 0px 0px 10px;
}

.basic-info{
  border: 1.5px solid #7E57C2;
  border-radius: 5px;
  box-shadow: 1px 1px 7px 0px #7E57C2;

}

.basic-info-title {
  box-sizing: border-box;
  height: 100%;
  padding: 0px;
}
</style>