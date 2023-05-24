<template>
  <div class="d-flex justify-content-center mt-5">
    <div class="signup">
      <div class="signup-title">
        <h2 class="pt-3">Sign Up</h2>
      </div>

      <div class="form-box d-flex align-items-center justify-content-center">
        <form @submit.prevent="signUp">
          <div class="mt-4 d-flex">
            <label for="signupusername" class="form-label margin-custom" style="font-size:17px;">
              <i class="fa-solid fa-lg fa-circle-user" style="color:#424242;"></i>
            </label>
            <input type="text" class="form-control ms-3 me-3" id="signupusername" aria-describedby="emailHelp" v-model="username" placeholder="ID">
          </div>

          <div class="mt-4 d-flex">
            <label for="nickname" class="form-label margin-custom" style="font-size:17px;">
              <i class="fa-solid fa-paw fa-lg" style="color:#424242;"></i>
            </label>
            <input type="text" class="form-control ms-3 me-3" id="nickname" aria-describedby="emailHelp" v-model="nickname" placeholder="NICKNAME">
          </div>

          <div class="mt-4 d-flex">
            <label for="email-1" class="form-label margin-custom" style="font-size:17px;"><i class="fa-solid fa-envelope fa-lg" style="color:#424242;"></i></label>
            <input type="text" class="form-control ms-3 me-3" id="email-1" aria-describedby="emailHelp" v-model="email" placeholder="EMAIL">
          </div>
          
          <div class="mt-4 d-flex">
            <label for="password1" class="form-label margin-custom" style="font-size:17px;">
              <i class="fa-solid fa-lock fa-lg" style="color:#424242;"></i>
            </label>
            <input type="password" class="form-control ms-3 me-3" id="password1" aria-describedby="emailHelp" v-model="password1" placeholder="PASSWORD">
          </div>

          <div class="mt-4 d-flex">
            <label for="password2" class="form-label margin-custom" style="font-size:17px;">
              <i class="fa-solid fa-unlock fa-lg" style="color:#424242;"></i>
            </label>
            <input type="password" class="form-control ms-3 me-3" id="password2" aria-describedby="emailHelp" v-model="password2" placeholder="PASSWORD CONFIRMATION">
          </div>

          <div class="d-flex justify-content-end mt-4">
            <button class="btn" style="background-color:#7E57C2; color: white;">OK</button>
          </div>
        </form>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username : null,
      nickname : null,
      email : null,
      password1 : null,
      password2 : null,
    }
  },
  methods: {
    signUp(){
      const username = this.username
      const password1 = this.password1
      const nickname = this.nickname
      const password2 = this.password2
      const email = this.email

      if (!username) {
        alert("ID를 입력해주세요!")
      }

      if (!nickname) {
        alert("NICKNAME을 입력해주세요!")
      }

      if (!email) {
        alert("EMAIL을 입력해주세요!")
      }

      if (!password1) {
        alert("PASSWORD를 입력해주세요!")
      }

      if (!password2) {
        alert("PASSWORD CONFIRMATION을 입력해주세요!")
      }

      const payload = {
        username, nickname, email, password1, password2
      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style scoped>
.signup {
  height: 500px;
  width: 450px;
  background-color: white;
  box-shadow: 1px 1px 10px 3px #7E57C2;
  border: 1px solid #7E57C2;
  border-radius: 10px;
}

.signup-title {
  height: 60px;
  width: 100%;
  background-color: #7E57C2;
  border-top-left-radius: 7px;
  border-top-right-radius: 7px;

  color: white;
}

.margin-custom {
  margin: 6px 0px 0px 18px;
}

.form-box {
  height: 420px;
}

input {
  width: 330px;
}
</style>