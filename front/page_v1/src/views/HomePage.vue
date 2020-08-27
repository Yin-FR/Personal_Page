<!--主业-->
<template>
    <div id="homePage">
        <div>
            <!--点击图片实现路由跳转-->
            <img width="100%" src="https://personal-page-tan.oss-cn-beijing.aliyuncs.com/imgs/brestPage.jpg"
                 alt="img" @click="selectImg(0)"/>
            <img width="100%" src="https://personal-page-tan.oss-cn-beijing.aliyuncs.com/imgs/DairyPage.jpg"
                 alt="img" @click="selectImg(1)"/>
            <img width="100%" src="https://personal-page-tan.oss-cn-beijing.aliyuncs.com/imgs/projectPage.jpg"
                 alt="img" @click="selectImg(2)"/>
        </div>
        <!--版权信息-->
        <div class="copyright">
            <p > Copyright © 2020 Yin . All rights reserved. </p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "HomePage",
        methods: {
            selectImg(index){
                if (index === 0){
                    this.$router.push('/main/album');
                } else if (index === 1){
                    this.$router.push('/main/dairy');
                } else if (index === 2){
                    this.$router.push('/main/project');
                } else {
                    this.$router.push('/main/comment')
                }
            }
        }
    }
</script>

<style scoped>
    .copyright{
        font-family: "Times New Roman";
        /*margin-bottom: 5px;*/
        height: 1.5em;
        padding: 0.5em;
        line-height: 1em;
    }


    img{
        margin-top: 0;
        padding: 0;
    }
</style>