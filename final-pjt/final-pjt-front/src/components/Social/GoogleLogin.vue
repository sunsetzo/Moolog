<template>
  <div>
    <button @click="loginWithGoogle">구글 소셜 로그인</button>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  methods: {
    loginWithGoogle: function() {
      const clientID = '128235535893-g8hd1udjg84ra9i1ke4aov3hhjkhv1g2.apps.googleusercontent.com';
      const redirectURL = 'http://localhost:8080/';

      // 구글 소셜 로그인 URL 생성
      const googleLoginURL = 'https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=' + clientID + '&redirect_uri=' + redirectURL + '&scope=email%20profile';

      // 새 창에서 구글 소셜 로그인 페이지 열기
      window.open(googleLoginURL, '_self');

    },
    
    processGoogleUserInfo: function(code) {
      // var self = this;
      console.log(code)
      // 서버로 구글 사용자 정보를 요청하기 위한 POST 요청 보내기
      axios.get('https://www.googleapis.com/oauth2/v2/userinfo?access_token=${access_token}', {headers: { "content-type": "application/x-www-form-urlencoded" }, code: code })
        .then(function(response) {
          // 응답 처리
          console.log(response.data);
          console.log('google login success')
          // DB에 성공적으로 저장되었거나 추가 작업을 수행

          // 처리 후 메인 홈으로 이동
          window.location.href = 'http://localhost:8080/';
        })
        .catch(function(error) {
          console.error(error);
          console.log('google login error')
          // 에러 처리
        });
    }
  },
  
  created: function() {
    // URL 파라미터에서 code 추출
    // console.log('created 호출')
    var params = new URLSearchParams(window.location.search);
    var code = params.get('code');

    if (code) {
      // code가 존재할 경우 구글 사용자 정보 처리
      this.processGoogleUserInfo(code);
    }
  }
}
</script>
