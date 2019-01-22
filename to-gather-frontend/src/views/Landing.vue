<template>
  <div>
    <div class="landing" >
      <div v-if="loginFail" class="failMessage">{{failMessage}}
          <div class="retbut" @click="ret()">返回</div>
      </div>
      <img src="https://static.muxixyz.com/loading.png" />
      <div class="landing-text">正在尝试登陆</div>
      <div class="landing-text">99%</div>
    </div>
  </div>
</template>
<script>
import cookie from "../cookie";

export default {
  name: 'landing',
  data(){
    return{
      loginFail: false,
      failMessage: '学号或密码错误'
    }
  },
  mounted(){
    const data = {
      "std_num": cookie.getCookie('stunum'),
      "password": cookie.getCookie('password'),
      "username": cookie.getCookie('username')
    }
    // console.log(data);
    fetch(`/api/v1.0/auth/login/`, {
        method: 'POST',
        headers: {
          "Content-Type":"application/json"
        },
        body: JSON.stringify(data),
      }).then(res => {
        if (res.ok){
          return res.json()
        }else{
          if(res.status == 401){
            this.loginFail = true;
          }else{
            this.failMessage = '登录失败'
            this.loginFail = true;
          }
        }
      }).then(res => {
        // localStorage.setItem('token', res.token);
        // localStorage.login = true;
        cookie.setCookie('token', res.token);
        cookie.setCookie('login', true);
        cookie.setCookie('landing', false);
        this.ret();
      })
      // .catch(err => {
      
      // })
  },
  methods:{
    ret(){
      let path = '/'
      if(this.$route.params.path){
        path = this.$route.params.path === '/' ? '/': this.$route.params.path;
      }
      this.$router.push(path);
    }
  }
}
</script>

<style scoped>
img{
  width: 64px;
  margin-top: 50%;
}
.landing{
  background: center / cover no-repeat url("https://static.muxixyz.com/bg.png");
  height: 100vh;
  text-align: center;
}

.landing-text{
  font-size: 18px;
  color: #FFFFFF;
}

.failMessage{
  width:328px;
  background: #FFFFFF;
  margin: 0 auto;
  border:1px solid rgba(0,0,0,0.12);
  border-radius: 3px;
  padding: 40px 0;
  text-align: center;
  box-sizing: border-box;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  color: #6200EE;
}
.retbut{
  width: 96px;
  height: 36px;
  line-height: 36px;
  text-align: center;
  margin: 0 auto;
  margin-top: 50px;
  font-size: 14px;
  border:1px solid rgba(0,0,0,0.12);
  border-radius: 5px;
}
</style>
