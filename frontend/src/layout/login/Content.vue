<template>
  <div class="login-custom-content">
    <fade-transition :duration="100" mode="out-in">
      <!-- your content here -->
      <card class="login-custom center-block">
        <div slot="header" class="card-header-primary text-center">
          <img src="@/assets/images/faceinit_logo_login.png" width="350px">
        </div>
        <form @submit.prevent="onSubmit(username, password)">
          <base-input label="아이디"
                      placeholder="ID"
                      v-model="username">
          </base-input>
          <base-input label="비밀번호"
                      type="password"
                      placeholder="PW"
                      v-model="password">
          </base-input>
          <base-button class="animation-on-hover" block native-type="submit" type="success">로그인</base-button>
        </form>
    </card>
    </fade-transition>
  </div>
</template>
<script>
/* eslint-disable */
  import {FadeTransition} from 'vue2-transitions';
  export default {
    components: {
      FadeTransition
    },
    data() {
      return {
        username : '',
        password : '',
        msg: ''
      }
    },
    methods: {
      onSubmit (username, password) {
        // LOGIN 액션 실행
        this.$store.dispatch('LOGIN', {username, password})
          .then(() => this.redirect())
          // eslint-disable-next-line
          .catch(({message}) => 
            console.log("hello")
          )
      },
      redirect () {
        this.$router.push('/')
      }
  }
  };
</script>
<style lang="scss">
.login-custom-content{
  padding: 78px 150px 30px 150px;
}

@media screen and (max-width: 768px){

  .login-custom-content {
    padding-left: 15px;
    padding-right: 15px;
  }

}

.login-custom{
  font-family: my-icons;
  font-size: 30pt;
  max-width : 800px;
  margin : auto;
}

@font-face {
  font-family: "my-icons";
  src: url('../../assets/fonts/NanumSquareRoundB.ttf') format('truetype'),;
}
</style>
