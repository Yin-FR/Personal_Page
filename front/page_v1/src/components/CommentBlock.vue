<!--PC端留言块-->
<template>
    <div id="commentBlock">
        <div id="timePart"><div class="innerWord">{{timeComment}}</div></div> <!--时间-->
        <div id="userPart"><div class="innerWord">{{userName}}</div></div> <!--user name-->
        <div id="contentPart"><div class="innerWord">{{contentComment}}</div></div> <!--内容-->
    </div>
</template>

<script>
    export default {
        name: "CommentBlock",
        props: {
            timeComment: String,
            userName: String,
            contentComment: String
        },
    }
</script>

<style scoped>
    #commentBlock{
        border-radius: 10px;
        border: 1px dashed #2c3e50;
        margin: 30px 10px;
        height: 30%;
        line-height: 1.5em;
    }

    #timePart{
        height: 100%;
        float: left;
        width: 30%;
        box-sizing: border-box;
        padding: 2px;
        word-break: break-all;
        display: flex;
        overflow: auto;
        border-right: 1px dotted gray;
    }

    #userPart{
        box-sizing: border-box;
        height: 100%;
        float: left;
        width: 30%;
        padding: 2px;
        word-break: break-all;
        display: flex;
        overflow: auto;
        border-right: 1px dotted gray;
    }

    #contentPart{
        height: 100%;
        float: left;
        width: 40%;
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