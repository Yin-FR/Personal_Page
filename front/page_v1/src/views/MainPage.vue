<template>
    <div id="mainPage">
        <el-container>
            <el-header>
                <Navi></Navi>
            </el-header>
            <el-main style="height: 100%">
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