<template>
  <div class="tab">
    <div class="mask" v-if="switchClick" @click="showSwitch()"></div>
    <router-link to="/" class="tab-item">
      <img class="tab-icon" src="https://static.muxixyz.com/tab_1.png" />
      <div class="tab-text">Universe</div>
    </router-link>
    <div class="tab-item" v-on:click="showSwitch()">
      <div class="switch" v-if="switchClick" >
        <div class="switch-container">
          <router-link :to="{ name: 'personal', params: { page: 'post' }}" class="switch-item">Post-Activity</router-link>
          <hr />
          <router-link :to="{ name: 'personal', params: { page: 'pick' }}" class="switch-item">Pick-Activity</router-link>
        </div>
        <div class="switch-arrow"></div>
      </div>
      <img class="tab-icon" src="https://static.muxixyz.com/tab_2.png" />
      <div class="tab-text">U&Me</div>
    </div>
  </div>
</template>
<script>

export default {
  name: 'Tab',
  data(){
    return{
      switchClick: false,
    }
  },
  methods:{
    showSwitch(){
      this.switchClick = !this.switchClick;
    },
  }
}
</script>
<style scoped>

.tab{
  width: 100%;
  height: 56px;
  background: #6200EE;
  font-size: 12px;
  vertical-align: middle;
  position: fixed;
  bottom: 0;
  display:table
}
.tab-item{
  display: table-cell;
  width: 50%;
  text-align: center;
  vertical-align: middle;
}
.tab-icon{
  width: 32px;
}
.tab-text{
  color: #ffffff;
  display: block;
  text-decoration: none;
}
.switch{
  width: 50%;
  position: absolute;
  bottom: 56px;
  background-color: transparent;
  font-size: 16px;
}
.switch-container{
  margin: 0 10%;
  padding: 10px;
  border-radius: 10px;
  background: #FFF;
}
.switch-item{
  line-height: 20px;
  display: block;
}
.switch-arrow{
  width: 0;
  height: 0;
  border: 6px solid transparent;
  border-top: 12px solid #FFF;
  margin: 0 auto;
}
a{
  text-decoration: none;
  color: #666666;
}
a:visited{
  color: #666666;
}
.mask{
  background-color: rgba(0, 0, 0, .5);
  position: fixed;
  width: 100%;
  height:100%;
  top:0;
  left: 0;
  /* z-index: 99; */
  display: table;
}
</style>
