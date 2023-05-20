<template>
    <div>
        <button @click="loginWithNaver">네이버 소셜 로그인</button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'NaverLogin',
    methods: {
        loginWithNaver() {
        axios.post('http://127.0.0.1:8000/accounts/allauth/naver/login/')
            .then(response => {
            // 요청 성공 시 처리할 로직 작성
            console.log(response.data);
            })
            .catch(error => {
            // 요청 실패 시 처리할 로직 작성
            console.error(error);
            });
        }
}
}
</script>