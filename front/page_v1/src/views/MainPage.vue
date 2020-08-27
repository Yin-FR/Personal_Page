<!--欢迎页后的总网页-->
<template>
    <div id="mainPage">
        <!--el-container实现容器布局-->
        <el-container>
            <el-header>
                <!--导航-->
                <Navi></Navi>
            </el-header>
            <el-main style="height: 100%">
                <!--导航下的路由窗口-->
                <router-view></router-view>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    import Navi from "../components/Navi";
    export default {
        name: "MainPage",
        components: {Navi}
    }
</script>

<style scoped>
    .el-container{
        box-sizing: border-box;
        height: 100%;
    }

    .el-main{
        box-sizing: border-box;
        padding: 0;
        line-height: 0;
    }

    #mainPage{
        box-sizing: border-box;
    }


</style>