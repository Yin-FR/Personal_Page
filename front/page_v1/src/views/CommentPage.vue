<!--留言页-->
<template>
    <div id="commentPage">
        <div class="intro">
            <p style="margin: auto">欢迎给我留言！😝</p>
        </div>

        <div class="commentShowArea">
            <CommentBlock v-if="!isMobile"
                          v-for="comment in commentsGroup"
                          :key="comment.timeSend"
                          :time-comment="comment.timeSend"
                          :user-name="comment.userNameSend"
                          :content-comment="comment.messageSend">
            </CommentBlock> <!--pc和pad端留言显示区域-->
            <CommentBlockMobile v-if="isMobile"
                          v-for="comment in commentsGroup"
                          :key="comment.timeSend"
                          :user-name="comment.userNameSend"
                          :content-comment="comment.messageSend">
            </CommentBlockMobile> <!--移动端留言显示区域，不包含留言时间-->
        </div>

        <div class="writeArea">
            <el-input v-model="userToBeSent" placeholder="昵称" clearable class="user_toBeSent"></el-input>
            <el-input v-model="contentToBeSent" placeholder="留言" clearable class="content_toBeSent"></el-input>
            <el-button class="sendBtn" type="primary" plain @click="sendComment">发送&emsp;&emsp;&emsp;<i class="el-icon-message"></i></el-button>
        </div> <!--编辑留言区域-->

    </div>
</template>

<script>
    import CommentBlock from "../components/CommentBlock";
    import CommentBlockMobile from "../components/CommentBlockMobile";
    export default {
        name: "CommentPage",
        components: {CommentBlockMobile, CommentBlock},
        data() {
            return {
                userToBeSent: '',
                contentToBeSent: '',
                commentsGroup: [],
                device: this.$store.state.device
            }
        },
        computed: {
            isMobile: function () {
                if (this.device === 'mobile'){
                    return 1
                } else {
                    return 0
                }
            }, /*判断登陆设备是否为移动端*/
        },
        methods: {
            getAllComments(){
                const axiosAjax = this.axios.create({
                    timeout: 1000*60,
                    withCredentials: true /*跨域许可*/
                });
                axiosAjax.get("http://47.98.136.14:4100/communication/comments").then((res)=>{
                    this.commentsGroup = res.data;
                }).catch((err)=>{
                    console.log(err);
                }) /*获取留言*/
            },
            sendComment(){
                let userSend = this.userToBeSent;
                let contentSend = this.contentToBeSent;
                if (userSend && contentSend){
                    let commentObj = {
                        user: userSend,
                        comment: contentSend
                    };
                    let config = {
                        header: {
                            'Content-Type':'application/json'
                        }
                    };
                    this.userToBeSent = '';
                    this.contentToBeSent = '';
                    const axiosAjax = this.axios.create({
                        timeout: 1000*60,
                        withCredentials: true
                    });
                    axiosAjax.post('http://47.98.136.14:4100/communication/comments', commentObj, config).then((res)=>{
                        this.$notify({
                            title: "留言成功",
                            type: "success",
                            message: "谢谢～🙏",
                            duration: 2000
                        });
                        this.getAllComments();
                    }).catch((err)=>{
                        console.log(err)
                    });
                } else {
                    this.$notify({
                        title: "留言失败",
                        type: "error",
                        message: "请填写完昵称和留言内容",
                        duration: 2000
                    })
                }

            } /*发送留言*/
        },
        mounted() {
            this.getAllComments(); /*页面渲染完成后获取留言*/
        }
    }
</script>

<style scoped>
    #commentPage{
        line-height: 60px;
        height: 100%;
    }

    .commentShowArea{
        box-sizing: border-box;
        height: 70%;
        background-color: white;
        overflow: auto;
        border-radius: 30px;
        padding: 5px;
        margin-left: 15px;
        margin-right: 15px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }

    .writeArea{
        box-sizing: border-box;
        height: 20%;
        padding: 15px 25px 25px;
        line-height: 4em;
    }

    .user_toBeSent{
        width: 28%;
        float: left;
    }

    .content_toBeSent{
        width: 68%;
        float: right;
    }

    .sendBtn{
        float: right;
    }

    .intro{
        height: 10%;
        display: flex;
    }
</style>