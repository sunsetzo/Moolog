<template>
  <div>
    <img src="@/assets/btn_google_signin_light_normal_web.png" alt="google"
    style="width:200px; height:50px" class="mb-1" @click="loginWithGoogle">
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'GoogleLogin',
  methods: {
    loginWithGoogle: function() {
      const clientID = '128235535893-g8hd1udjg84ra9i1ke4aov3hhjkhv1g2.apps.googleusercontent.com';
      const redirectURL = 'http%3A%2F%2Flocalhost%3A8080%2Fgoogle%2Flogin%2F';

      // 구글 소셜 로그인 URL 생성
      const googleLoginURL = 'https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=' + clientID + '&redirect_uri=' + redirectURL + '&scope=email%20profile';

      // 새 창에서 구글 소셜 로그인 페이지 열기
      window.open(googleLoginURL, '_self');

    },
    
    getGoogleToken(code){
      const Token_URL = 'http://www.oauth2.googleapis.com/token'
      const clientID = '128235535893-g8hd1udjg84ra9i1ke4aov3hhjkhv1g2.apps.googleusercontent.com';
      const clientSecret = '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'
      const redirectURL = 'http://localhost:8080/';
      axios({
        method:'post',
        url : Token_URL,
        data : {
          code, 
          client_id : clientID,
          client_secret : clientSecret,
          redirect_uri : redirectURL, 
          grant_type : 'authorization_code'
        }
      })
      .then((res)=>{
        console.log(res)
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
  
  created: function() {
    // URL 파라미터에서 code 추출
    // console.log('created 호출')
    const params = window.location.href
    const codeIdx = params.indexOf('code')
    const scopeIdx = params.indexOf('&scope')

    const code = params.substr(codeIdx+5, (scopeIdx-codeIdx-5))
    console.log(code)
    this.getGoogleToken(code)
    
  }
}
</script>

<<<<<<< HEAD
=======
<style scoped>
img {
  cursor: pointer;
}
</style>
>>>>>>> f3242b8073271f6577f24747711142bab784712c
