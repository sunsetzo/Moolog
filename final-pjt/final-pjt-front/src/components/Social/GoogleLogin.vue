<template>
<div>
  <button @click="handleGoogleLogin">구글 소셜 로그인</button>
</div>
</template>

<script>
import axios from 'axios';

export default {
  methods: {
    handleGoogleLogin() {
      const clientId = '128235535893-g8hd1udjg84ra9i1ke4aov3hhjkhv1g2.apps.googleusercontent.com'; // 구글 API 클라이언트 ID를 입력하세요.
      const redirectUri = 'http://127.0.0.1:8000/accounts/allauth/google/login/callback/'; // 구글 로그인 후 리디렉션될 URL을 입력하세요.

      const scopes = 'email%20profile'; // 수정된 스코프 값

      const authUrl = `https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=code&scope=${scopes}`;

      //https://accounts.google.com/o/oauth2/v2/auth?client_id=128235535893-g8hd1udjg84ra9i1ke4aov3hhjkhv1g2.apps.googleusercontent.com&redirect_uri=accounts/allauth/google/login/callback/&response_type=code&scope=email%20profile
      console.log(authUrl)

      window.location.href = authUrl;
    },
    handleLoginSuccess(code) {
      const url = 'http://127.0.0.1:8000/accounts/'; // Django API 엔드포인트 URL을 입력하세요.

      // Axios를 사용하여 Django 서버로 POST 요청 보내기
      axios.post(url, { code })
        .then(response => {
          // 요청 성공 시 동작할 코드 작성
          console.log(response.data);
        })
        .catch(error => {
          // 요청 실패 시 동작할 코드 작성
          console.error(error);
        });
    }
  },
  mounted() {
    // 리디렉션된 URL에서 쿼리 파라미터 "code"를 가져옴
    const code = new URLSearchParams(window.location.search).get('code');
    
    // "code" 파라미터가 있는 경우에만 로그인 성공 처리
    if (code) {
      this.handleLoginSuccess(code);
    }
  }
}
</script>