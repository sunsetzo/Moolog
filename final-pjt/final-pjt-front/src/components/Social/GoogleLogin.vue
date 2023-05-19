<!-- <template>
<div>
    <button @click="googleLogin">구글 로그인</button>
</div>
</template>

<script>
import axios from 'axios';

export default {
name: 'GoogleLogin',
created() {
    this.loadGoogleApi();
  },
methods: {
    loadGoogleApi() {
      window.gapi.load('auth2', () => {
        window.gapi.auth2.init({
          client_id: 'YOUR_GOOGLE_CLIENT_ID',
        });
      });
    },
    googleLogin() {
    gapi.load('auth2', () => {
        gapi.auth2.init({
        client_id: '128235535893-g8hd1udjg84ra9i1ke4aov3hhjkhv1g2.apps.googleusercontent.com',
        }).then(() => {
        gapi.auth2.getAuthInstance().signIn().then((googleUser) => {
            const id_token = googleUser.getAuthResponse().id_token;

            // 사용자 정보를 서버로 전송
            this.saveUserData(id_token);
        }).catch((error) => {
            console.error('구글 로그인 실패:', error);
        });
        });
    });
    },
    saveUserData(id_token) {
    // 서버로 데이터 전송
    axios.post('/api/google/user', { id_token })
        .then((response) => {
        console.log('데이터 저장 성공:', response.data);
        })
        .catch((error) => {
        console.error('데이터 저장 실패:', error);
        });
    },
},
};
</script> -->
