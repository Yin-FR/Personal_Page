<template>
    <div id="navi">
        <div id="naviPC" v-if="this.$store.state.device !== 'mobile'">
            <el-menu :default-active="pageSelected" class="el-menu-demo" router mode="horizontal">
                <el-menu-item index="/main/home">主页</el-menu-item>
                <el-menu-item index="/main/album">相册</el-menu-item>
                <el-menu-item index="/main/dairy">日志</el-menu-item>
                <el-menu-item index="/main/project">项目</el-menu-item>
                <el-menu-item index="/main/comment">留言</el-menu-item>
            </el-menu>
        </div>
        <div id="naviMobile" v-if="this.$store.state.device === 'mobile'">
            <el-menu :default-active="pageSelected" class="el-menu-demo" router mode="horizontal">
                <el-menu-item index="/main/home" class="mobilenavi"><i class="el-icon-house"></i></el-menu-item>
                <el-menu-item index="/main/album" class="mobilenavi"><i class="el-icon-camera"></i></el-menu-item>
                <el-menu-item index="/main/dairy" class="mobilenavi"><i class="el-icon-notebook-2"></i></el-menu-item>
                <el-menu-item index="/main/project" class="mobilenavi"><i class="el-icon-monitor"></i></el-menu-item>
                <el-menu-item index="/main/comment" class="mobilenavi"><i class="el-icon-edit"></i></el-menu-item>
            </el-menu>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Navi",
        computed: {
            pageSelected: function () {
                if(this.$route.path.replace('/','')==='main/home'){
                    return '/main/home';
                }
                else if(this.$route.path.replace('/','')==='main/album'){
                    return '/main/album'
                }
                else if(this.$route.path.replace('/','')==='main/dairy'){
                    return '/main/dairy'
                }
                else if(this.$route.path.replace('/','')==='main/project'){
                    return '/main/project'
                }
                else{
                    return '/main/comment'
                }
            }
        }
    }
</script>

<style scoped>
    .mobilenavi{
        padding-left: 5%;
        padding-right: 5%;
    }
</style>