<template>
<div class="message">
    <div class="wrongPage" v-if="success" @click='closeWrong'>
        {{WrongMessage}}
    </div>
    <div class="datilCard" v-if="!success">
        <img class="last" @click='ret' src="https://static.muxixyz.com/back.png" />
        <img class="next" @click='next' src="https://static.muxixyz.com/next.png" />
        <div class="actionTime aciton-detail">
            <span>Time/</span>
            <span class="left">{{datetime}}</span>
        </div>
        <div class="actionLocation aciton-detail">
            <span>Location/</span>
            <span class="left">{{location}}</span>
        </div>
        <div class="event aciton-detail">
            <span>Event/</span>
            <span class="left">{{event}}</span>
        </div>
        <div class="message-adds">
            <span>Adds/</span>
            <span class="left">{{question}}</span>
        </div>
        <div class="message-reply">
            <span>Reply/</span>
            <span class="left">{{answer}}</span>
        </div>
        <div class="message-btns">
            <button class="no button" @click='ret' >NO:(</button>
            <button class="yes button" @click='pass'>OK:)</button>
        </div>
    </div>
</div>
</template>

<script>
    import Cookie from '.././cookie.js'
    export default {
        name: 'messageReply',
        data(){
            return{
                WrongMessage: "",
                success: false,
                token:"",
                unum: "",
                aid: 0,
                position:0,
                datetime: "",
                location: "",
                event: "",
                question: "",
                answer: "",
                time: "",
                picker_id: "",
                readed: false,
                messageCount: 0,
                messageList: []
            }
        },
        mounted() {
            this.token = Cookie.getCookie('token'),
            this.unum = Cookie.getCookie('stunum'),
            this.aid = this.$route.params.aid,
            this.getReplyList(this.aid)
        },
        methods:{
            ret(){
                let path = '/'
                if(this.$route.params.path){
                    path = this.$route.params.path === '/' ? '/': this.$route.params.path;
                }
                this.$router.push(path);
            },
            closeWrong(){
                if(this.success == true){
                    this.success = false;
                    this.WrongMessage = ""
                }
            },
            next(){
                if(this.position === this.position + 1);
                else{
                    this.position = this.position + 1;
                    this.getReplyDetail(this.messageList[this.position]);
                }
            },
            getReplyList(aid){
                fetch(`/api/v1.0/user/${this.unum}/activity/${aid}/message/list/`,{
                    method:"GET",
                    headers:{
                        token: this.token,
                        "Content-Type": "application/json"
                    }
                }).then(res => {
                    if (res.status === 200) {
                        return res.json();
                    }
                    else if(res.status === 401){
                        this.$router.push({path:'/'})
                    }
                    else if(res.status === 406){
                        this.success = true,
                        this.WrongMessage = "该用户不存在"
                    }
                    else if(res.status === 407){
                        this.success = true,
                        this.WrongMessage = "请检查你自己的消息"
                    }
                }).then(res =>{
                    this.messageCount = res.messageCount,
                    this.messageList = res.messageList,
                    this.getReplyDetail(this.messageList[this.position])
                })
            },
            getReplyDetail(mid){
                fetch(`/api/v1.0/user/${this.unum}/message/${mid}/`,{
                    method:"GET",
                    headers:{
                        token: this.token,
                        "Content-Type": "application/json"
                    }
                }).then(res=>{
                    if (res.status === 200) {
                        return res.json();
                    }
                    else if(res.status === 401){
                        this.$router.push({path:'/'})
                    }
                    else if(res.status === 406){
                        this.success = true,
                        this.WrongMessage = "消息不见啦"
                    }
                    else if(res.status === 407){
                        this.success = true,
                        this.WrongMessage = "请检查你自己的消息"
                    }
                }).then(res => {
                    this.datetime = res.datetime,
                    this.time = res.time,
                    this.location = res.location,
                    this.event = res.event,
                    this.qq = res.qq,
                    this.tel = res.tel,
                    this.question = res.question,
                    this.answer = res.answer,
                    this.picker_id = res.picker_id,
                    this.readed = res.readed
                })
            },
            pass(){
                let message = {
                    "pickerID": this.picker_id,
                    "atti": true
                }
                fetch(`/api/v1.0/activity/${this.aid}/`,{
                    method:"PUT",
                    headers:{
                        token: this.token,
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(message)
                }).then(res=>{
                    if(res.status === 200){
                        this.$router.push({name:'personal', params:{page: 'post'}})
                    }
                })
            }
        }
    }
</script>

<style scoped>
.datilCard{
    width:87%;
    padding: 16px 7px;
    min-height: calc(100vh - 120px);
    border:1px solid rgba(0,0,0,0.12);
    border-radius: 3px;
    margin: 0 auto;
    top: 18px;
    position: relative;
    height: 100px;
    background-color: white;
    border: 2px; 
}
.last{
    width: 34px;
    height: 36px;
}
.next{
    width: 34px;
    height: 36px;
    float: right;
}
.aciton-detail{
    font-size: 14px;
    margin-top: 19px;
    margin-left: 19px;
    max-width: 278px;
}
.personalMessage{
    margin-top: 19px;
    margin-left: 19px;
}
.wrong{
    width: 95%
}
.tips{
    font-size: 10px;
    color: #6200EE;
    margin-top: 26px;
    margin-left: 19px;
}
.message-adds{
    margin-left: 19px;
    margin-top: 31px;
    color: #6200EE;
    font-size: 14px;
    font-weight: bold;
}
.message-reply{
    margin-left: 19px;
    margin-top: 18px;
    color: #6200EE;
    font-size: 14px;
    font-weight: bold;
}
.message-btns {
    height: 50px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 0 19px;
    align-items: center;
    margin-top: 19px;
}
.button{
    width: 96px;
    height: 36px;
    text-align: center;
    font-size: 14px;
    border:1px solid rgba(0,0,0,0.12);
    border-radius: 5px;
}
.no{
    background-color: #7286FA;
    color:white;
}
.yes{
    background-color: #E8E0FB;
    color: #3B00DD;
}
.wrongPage{
    width:328px;
    min-height:252px;
    background: #FFFFFF;
    margin: 0 auto;
    border:1px solid rgba(0,0,0,0.12);
    border-radius: 3px;
    padding: 120px 0;
    text-align: center;
    box-sizing: border-box;
    position: relative;
    top: 50%;
    transform: translateY(-50%);
    color: #6200EE;
}
</style>

