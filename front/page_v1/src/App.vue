<!--根组件-->
<template>
    <div id="app">
        <router-view style="height: 100%"></router-view>
    </div>
</template>

<script>

    export default {
        name: 'App',
        components: {},
        mounted() {
            let index = 0;
            /*页面渲染完毕则调用已经在vuex中的定义好的全局函数findDevice确定访问设备，并全局储存device变量以便后期使用*/
            this.$store.dispatch('findDevice', {index});
            /*由device变量决定路由将要跳转的欢迎页面*/
            if (this.$store.state.device !== 'mobile') {
                this.$router.push('/welcome')
            } else {
                this.$router.push('/welcomeM')
            }
        }
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 0;

        height: 100%;
    }
</style>
