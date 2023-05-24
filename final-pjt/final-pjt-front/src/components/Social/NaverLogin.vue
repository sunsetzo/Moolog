<template>
    <div>
      <img src="@/assets/btnG_완성형.png" alt="naver" style="width:194px; height:47px;" class="mb-2" @click="handleNaverLogin">
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'NaverLogin',
    created() {
      const params = new URLSearchParams(window.location.search);
      const code = params.get('code');
      const state = params.get('state');
  
      if (code && state) {
        console.log('네이버 로그인 성공');
        console.log('Authorization Code:', code);
        console.log('State:', state);
  
        // Django 서버에 사용자 정보 전송
        axios
          .post('https://nid.naver.com/oauth2.0/token', {
            params: {
              code: code,
              state: state
            }
          })
          .then(response => {
            console.log('사용자 정보 저장 성공:', response.data);
            // 여기서 창을 닫습니다.
            window.close();
          })
          .catch(error => {
            console.error('사용자 정보 저장 실패:', error);
          });
      }
    },
    methods: {
      handleNaverLogin() {
        const clientId = 'qbZ6_KhqIlCQqX9OXwEr';
        const callbackUrl = 'http://localhost:8080/';
        const authUrl = `https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id=${clientId}&redirect_uri=${callbackUrl}`;
  
        window.open(authUrl, '_blank', 'width=500,height=600');
      }
    }
  };
  </script>
  
  <style scoped>
  img {
    cursor: pointer;
  }
  </style>