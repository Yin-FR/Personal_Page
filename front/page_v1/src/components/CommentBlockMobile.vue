<!--移动端留言块-->
<template>
    <div id="commentBlockMobile">
        <div id="userPartMobile"><div class="innerWord">{{userName}}</div></div> <!--user name-->
        <div id="contentPartMobile"><div class="innerWord">{{contentComment}}</div></div> <!--内容-->
    </div>
</template>

<script>
    export default {
        name: "CommentBlockMobile",
        props: {
            userName: String,
            contentComment: String
        },
    }
</script>

<style scoped>
    #commentBlockMobile{
        border-radius: 10px;
        border: 1px dashed #2c3e50;
        margin: 30px 10px;
        height: 30%;
        line-height: 1.5em;
    }

    #userPartMobile{
        box-sizing: border-box;
        height: 100%;
        float: left;
        width: 35%;
        padding: 2px;
        word-break: break-all;
        display: flex;
        overflow: auto;
        border-right: 1px dotted gray;
    }

    #contentPartMobile{
        height: 100%;
        float: left;
        width: 65%;
        box-sizing: border-box;
        padding: 2px;
        word-break: break-all;
        display: flex;
        overflow: auto;
    }

    .innerWord{
        margin: auto;
        padding-left: 1em;
        padding-right: 1em;

    }

</style>