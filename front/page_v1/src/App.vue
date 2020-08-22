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
            this.$store.dispatch('findDevice', {index});
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
