<template>
  <div class="activities" ref="actBox">
    <login v-if="landing"/>
    <div class="act-item" 
      v-on:click="checklogin(activity.activityID)"  
      v-for = "activity in activityList" 
      :key="activity.id" 
      :class="{itemgrey: (activity.statu == 2 || activity.close || activity.success) }" 
    >
      <div class="act-time" :class="{actpass: activity.statu == 1}">
        <span v-if="page === 'pick'">{{statuList[activity.statu]}} - </span>
          {{activity.datetime}}
      </div>
      <div v-if="activity.hasMessage" class="reddot"></div>
      <div class="act-event">{{activity.event}}</div>
    </div>
    <div class="act-none" v-if="!rowsNum">这里空空如也，快去POST或PICK一个活动吧～</div>
    <div class="add-act" v-on:click="add" >+</div>
  </div>
</template>

<script>
import Login from '@/components/login.vue'
import cookie from "../cookie";

export default {
  name: 'Activities',
  props: {
    page: String,
  },
  components: {
    Login
  },
  data(){
    return{
      statuList: ['Waiting', 'Successful', 'Fail'],
      activityList: [],
      hasNext: false,
      pageMax: 1,
      pageNum: 1,
      rowsNum: 0,
      token: cookie.getCookie('token'),
      landing: cookie.getCookie('landing') == 'true',
      login: cookie.getCookie('login') == 'true',
    }
  },
  mounted() {
    if(this.page == 0){ //所有可以pick
      this.fetchPickable(1);
    } else {
      if(!this.login){
        this.landing = true;
      } else if(this.$route.path.split('/')[2] == 'post'){//我发起的activity
        this.fetchPost(1);
      } else if(this.$route.path.split('/')[2] == 'pick'){
        this.fetchPick(1);
      }
    }
    this.box = this.$refs.actBox;
    this.box.addEventListener('scroll',()=>{
      const divHeight = this.box.scrollHeight;
      const scrollTop = this.box.scrollTop;
      const barHeight = this.box.offsetHeight;
      if(scrollTop + barHeight === divHeight && this.hasNext){
        // console.log('!');
        this.pageNum++;
        if(this.page == 0){ //所有可以pick
          this.fetchPickable(1);
        } else {
          if(!this.login){
            this.landing = true;
          } else if(this.$route.path.split('/')[2] == 'post'){//我发起的activity
            this.fetchPost(1);
          } else if(this.$route.path.split('/')[2] == 'pick'){
            this.fetchPick(1);
          }
        }
      }
      
    });
  },
  methods:{
    checklogin(id){
      const el = this.activityList.filter((el)=>{
        return el.activityID == id;
      })[0];
      if(!this.login){
        this.landing = true;
      } else {
        if(this.page == '0'){
          this.$router.push({
            name: 'actionDetail',
            params:{
              aid: id,
              path: this.$route.path
            }
          });
        }else if (this.page == 'post' ){
          if(el.hasMessage){
            this.$router.push({
              name: 'messageReply',
              params:{
                aid: id,
                path: this.$route.path
              }
            });
          }else{
            this.$router.push({
              name: 'passDetail',
              params:{
                aid: id,
                path: this.$route.path
              }
            });
          }
        }else {
          if(el.statu == 1){
            this.$router.push({
              name: 'passDetail',
              params:{
                aid: id,
                path: this.$route.path
              }
            });
          }else{
            this.$router.push({
              name: 'actionDetail',
              params:{
                aid: id,
                path: this.$route.path
              }
            });
          }
        }
      }
    },
    fetchPickable(flag){
      fetch(`/api/v1.0/activity/pickable/list/?page=${this.pageNum}`, {
        method: 'GET',
        headers: {
          "Content-Type":"application/json"
        }
      }).then(res => {
        if (res.ok){
          return res.json()
        }
      }).then(res => {
        if(flag){
          this.activityList = this.activityList.concat(res.activityList);
        }else{
          this.activityList = res.activityList;
        }
        this.hasNext = res.hasNext;
        this.pageMax = res.pageMax;
        this.pageNum = res.pageNum;
        this.rowsNum = res.rowsNum;
      })
    },
    fetchPost(flag){
      const stuNum = cookie.getCookie('stunum');
      let page = 1;
      if(this.pageNum){
        page = this.pageNum;
      }
      fetch(`/api/v1.0/user/${stuNum}/post-activities/list/?page=${page}`, {
        method: 'GET',
        headers: {
          "Content-Type":"application/json",
          token: this.token
        }
      }).then(res => {
        if (res.ok){
          return res.json()
        }
      }).then(res => {
        if(flag){
          this.activityList = this.activityList.concat(res.activityList);
        }else{
          this.activityList = res.activityList;
        }
        this.hasNext = res.hasNext;
        this.pageMax = res.pageMax;
        this.pageNum = res.pageNum;
        this.rowsNum = res.rowsNum;
      })
    },
    fetchPick(flag){
      let page = 1;
      if(this.pageNum){
        page = this.pageNum;
      }
      const stuNum = cookie.getCookie('stunum');
      fetch(`/api/v1.0/user/${stuNum}/pick-activities/list/?page=${page}`, {
        method: 'GET',
        headers: {
          "Content-Type":"application/json",
          token: this.token
        }
      }).then(res => {
        if (res.ok){
          return res.json()
        }
      }).then(res => {
        if(flag){
          this.activityList = this.activityList.concat(res.activityList);
        }else{
          this.activityList = res.activityList;
        }
        this.hasNext = res.hasNext;
        this.pageMax = res.pageMax;
        this.pageNum = res.pageNum;
        this.rowsNum = res.rowsNum;
      })
    },
    add(){
      if(!this.login){
        this.landing = true;
      } else {
        this.$router.push({
          name: 'newActivity',
          params:{
            path : this.$route.path
          }
        });
      }
    },
  },
  watch: {
    '$route': function(){
      this.landing = cookie.getCookie('landing') == 'true'; //更新landing状态
      //重新获取数据
      const page = this.$route.path.split('/')[2];
      if(this.page == 0){ //所有可以pick
        this.fetchPickable(0);
      } else {
        this.page = page;
        // console.log(this.page);
        if(!this.login){
          this.landing = true;
        } else if(page == 'post'){//我发起的activity
          this.fetchPost(0);
        } else if(page == 'pick'){
          this.fetchPick(0);
        }
      }
    },
  },
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.activities{
  padding-top: 18px ;
  height: calc(100vh - 56px);
  overflow-y: scroll;
  box-sizing: border-box;
}
.act-item{
  background: #FFFFFF;
  width: 80vw;
  height:72px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 3px;
  margin-bottom: 16px;
  position: relative;
}
.act-time{
  font-size:14px;
  color:rgba(0,0,0,0.6);
  line-height:20px;
}
.act-event{
  font-size:16px;
  line-height:22px;
  color: #4A4A4A;
  margin-top: 3px;
}
.act-none{
  text-align: center;
  color: #FFFFFF;
  font-size: 20px;
  padding: 0 20px;
}
.add-act{
  width:56px;
  height:56px;
  border-radius: 50%;
  background: #6200EE;
  color: #FFFFFF;
  position: absolute;
  right: 24px;
  bottom: 70px;
  font-size:36px;
  line-height: 56px;
  text-align: center;
}
.itemgrey{
  /* opacity: 0.75; */
  background: #dddddd;
}
.actpass{
  color: #6200EE;
}
.reddot{
  background: #FF001F;
  width: 15px;
  height: 15px;
  border-radius: 50%;
  position: absolute; 
  top: -7.5px;
  right: -7.5px;
}
</style>
