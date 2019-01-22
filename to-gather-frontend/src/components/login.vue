<template>
  <div class="login-mask">
    <div class="login-wrapper">
      <div class="login-container">
        <div class="login-title">身份信息核验</div>
        <img src='https://static.muxixyz.com/close.png' class="login-close" @click="close()" />
        <div class="inp-container" v-bind:class="{focus: focusName}">
          <input class="login-inp" placeholder="Name_姓名" @focus="handleFocus(0)" @blur="handleNotFocus(0)" v-model="username"/>
          <img class="login-icon" v-bind:src="[focusName ? nameIconfocus: nameIcon]" />
        </div>
        <div class="inp-container" v-bind:class="{focus: focusId}" >
          <input class="login-inp" placeholder="ID_学号" @focus="handleFocus(1)" @blur="handleNotFocus(1)" v-model="stunum"/>
          <img class="login-icon" v-bind:src="[focusId ? idIconfocus: idIcon]" />
        </div>
        <div class="inp-container" v-bind:class="{focus: focusPw}" >
          <input type="password" class="login-inp" placeholder="Password_密码" @focus="handleFocus(2)" @blur="handleNotFocus(2)" v-model="password"/>
          <img class="login-icon" v-bind:src="[focusPw ? idIconfocus: idIcon]" />
        </div>
        <div class="login-tip">*tips 信息仅用于Check-in，不会以任何方式泄露至宇宙中</div>
        <div class="login-but" v-on:click="login()" >Done</div>
        <div class="input-none" v-if="none">任何一项不能为空！</div>
      </div>
    </div>
  </div>
</template>

<script>
import cookie from "../cookie";
export default {
  name: 'Login',
  inject: ['reload'],
  data(){
    return{
      nameIcon: "https://static.muxixyz.com/name.png",
      nameIconfocus: "https://static.muxixyz.com/name_focus.png",
      idIcon: "https://static.muxixyz.com/num.png",
      idIconfocus: "https://static.muxixyz.com/num_focus.png",
      focusName: false,
      focusId:false,
      focusPw:false,
      username: "",
      stunum: "",
      password: "",
      none: false,
    }
  },
  props: {
    name: String,
    id: Number
  },
  methods:{
    handleFocus(value){
      if(value == 2){
        this.focusPw = true;
      } else if (value == 1){
        this.focusId = true;
      } else {
        this.focusName = true;
      }
    },
    handleNotFocus(value){
      if(value == 2){
        this.focusPw = false;
      } else if (value == 1){
        this.focusId = false;
      } else {
        this.focusName = false;
      }
    },
    login(){
      if(this.username != '' && this.stunum != '' && this.password != ''){
        cookie.setCookie('username', this.username);
        cookie.setCookie('stunum', this.stunum);
        cookie.setCookie('password', this.password);
        cookie.setCookie('landing', false);
        this.$router.push({
          name: 'landing',
          params:{
            path : this.$route.path
          }
        });
      } else {
        this.none = true;
      }

    },
    close(){
      cookie.setCookie('landing', false);
      if(this.$route.path.split('/')[1] != ''){
        this.$router.push('/');
      } else {
        this.reload();
      }
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login-mask{
  background-color: rgba(0, 0, 0, .5);
  position: fixed;
  width: 100%;
  height:100%;
  top:0;
  left: 0;
  z-index: 99;
  display: table;
}
.login-wrapper{
  display: table-cell;
  vertical-align: middle;
}
.login-container{
  width: 80vw;
  min-height:252px;
  background: #FFFFFF;
  margin: 0 auto;
  border:1px solid rgba(0,0,0,0.12);
  border-radius: 5px;
  padding: 16px;
  box-sizing: border-box;  
}
.login-close{
  width: 18px;
  height: 20px;
  float: right;
}
.login-title{
  font-size:18px;
  display: inline-block;
}
.login-inp{
  width: 80%;
  height:30px;
  font-size:16px;
  line-height:30px; 
  margin-top: 20px;
  border: none;
  outline: none;
  margin-left: 0;
}
.inp-container{
  width: 100%;
  /* width:288px; */
  border-bottom: 2px solid #878787;
}
.focus{
  border-bottom: 2px solid #6200EE;
}
.login-icon{
  width: 24px;
  margin-top: 25px;
  float: right;
}
.login-tip{
  font-size:10px;
  line-height:1.4em;
  margin-top: 20px;
}
.login-but{
  width:96px;
  height:36px;
  background:rgba(232,224,251,1);
  border-radius:4px;
  line-height: 36px;
  text-align: center;
  margin: 0 auto;
  margin-top: 10px;
  color: #6200EE;
}
.input-none{
  font-size:14px;
  text-align: center;
  color: #878787;
}
</style>
