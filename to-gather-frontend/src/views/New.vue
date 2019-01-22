<template>
    <div class="new">
        <img class="back" @click='prev' src="https://static.muxixyz.com/back.png" />
        <div class="content">
            <div class="new-date">
                <!-- <el-date-picker 
                    v-model="date" 
                    type="date" 
                    @change="formatTime" 
                    value-format="yyyy-MM-dd"                    
                    placeholder="Date_日期" 
                    style="width:94%;" 
                    :picker-options="pickerOptions1">
                </el-date-picker> -->
                <Datepicker 
                    v-model="date" 
                    :disabledDates="disabledDates"
                    format="yyyy-MM-dd" 
                    placeholder="Date_日期" 
                    input-class="font margin"
                    calendar-class="canlendar"
                >
                </Datepicker>
            </div>
            <input placeholder="Time_时间" v-model="time" class="new-time font margin" />
            <input placeholder="Event_事件" v-model="event" class="new-event font margin" />
            <div class="newTips">*tips 以下信息仅在你二次确认之后，才将被对方接收</div>
            <input placeholder="Place_碰头地" v-model="location" class="new-place font margin" />
            <input placeholder="QQ_神奇编码" v-model="qq" class="new-qq font margin" />
            <input placeholder="Tel_电话" v-model="tel" class="new-tel font margin" />
            <input placeholder="Adds_还想说点啥" v-model="question" class="new-adds font" />
            <div class="input-none" v-if="none">*tips 任何一项不能为空！</div>
        </div>
        <div class="new-card-btns">
            <button class="no button" @click='prev'>NO:(</button>
            <button class="yes button" @click='alter'>OK:)</button>
        </div>
    </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker';

import Cookie from '.././cookie.js'
export default {
    name: 'newActivity',
    data(){
        return{
            pickerOptions1: {
                disabledDate(time) {
                    return time.getTime() < Date.now();
                }
            },
            date: "",
            none: false,
            year: "",
            month: "",
            day: "",
            time: "",
            location: "",
            event:"",
            qq:"",
            tel:"",
            question:"",
            disabledDates: {
                to: new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate()), // Disable all dates up to specific date
            }

        }
    },
    components:{
        Datepicker
    },
    mounted() {
        this.token = Cookie.getCookie('token')
    },
    methods:{
        prev(){
            let path = '/'
                if(this.$route.params.path){
                    path = this.$route.params.path === '/' ? '/': this.$route.params.path;
                }
            this.$router.push(path);
        },
        alter(){
            // console.log(this.date.getFullYear());
            

            if(this.date && this.time != '' && this.location != '' && this.event != '' && this.qq != '' && this.tel !='' && this.question !=''){
                this.year = parseInt(this.date.getFullYear());
                this.month = parseInt(this.date.getMonth()) + 1;
                this.day = parseInt(this.date.getDate());
                var message = {
                    "year": this.year,
                    "month": this.month,
                    "day": this.day,
                    "time": this.time,
                    "location": this.location,
                    "event": this.event,
                    "qq": this.qq,
                    "tel": this.tel,
                    "question": this.question
                }
                fetch(`/api/v1.0/activity/post/`,{
                    method: "POST",
                    headers:{
                        token: this.token,
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(message),
                }).then(res=>{
                    if(res.status === 200)
                        this.$router.go(-1)
                })
            }else{
                this.none = true;
            }
        }
    },
}
</script>

<style >
.cell.selected {
    background-color:#E8E0FB !important;
}
.new{
    width:87%;
    padding: 16px 7px;
    min-height: 500px;
    border:1px solid rgba(0,0,0,0.12);
    border-radius: 3px;
    margin: 0 auto;
    top: 18px;
    position: relative;
    /* height: 100px; */
    background-color: white;
    border: 2px; 
    z-index: 100;
}
/* .new-date /deep/ .el-input__inner{
        width:96%;
        margin-left: 5px;
        height: 40px;
        outline:none;
        border: none;
        border-radius:0;
        border-bottom: 2px solid #878787;
        color: #878787;
}
.new-date /deep/ .el-input__inner:focus{
    border-bottom: 2px solid #6200EE;

} */
.back{
    width: 34px;
    height: 36px;
}
.content{
    margin-left: 19px;
}
.font{
    font-size: 14px;
    color:#878787;
    width: 90%;
}
.margin{
    margin-top: 10px;
}
.new-adds{
    margin-top: 30px;
}
input{
    height: 30px;
    outline:none;
    border: none;
    border-bottom: 2px solid #878787;
    margin-left: 5px;
}
input:focus {
    border-bottom: 2px solid #6200EE;
}
.newTips{
    color: #6200EE;
    font-size: 10px;
    margin-top: 38px;
}
.button{
    width: 96px;
    height: 36px;
    text-align: center;
    font-size: 14px;
    border:1px solid rgba(0,0,0,0.12);
    border-radius: 5px;
}
.new-card-btns {
    height: 50px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 0 19px;
    align-items: center;
    margin-top: 19px;
}
.input-none{
  font-size:10px;
  color: #878787;
  margin-top: 10px;
}
.no{
    background-color: #7286FA;
    color:white;
}
.yes{
    right: 42px;
    background-color: #E8E0FB;
    color: #3B00DD;
}
</style>


