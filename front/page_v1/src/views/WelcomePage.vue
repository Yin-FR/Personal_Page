<template>
    <div id="welcomePage">
        <el-container>
            <el-main>
                <div style="height: 100%">
                    <transition-group name="fade" tag="p">
                        <p :key="0" v-show="this.shows.one">嗨</p>
                        <p :key="1" v-show="this.shows.two">您好</p>
                        <p :key="2" v-show="this.shows.three">欢迎光临</p>
                        <p :key="3" v-show="this.shows.four">期待我们的合作</p>
                    </transition-group>
                </div>
            </el-main>
            <el-footer>
                <div id='footSpace'>
                    <transition name="fade">
                        <router-link to="/main" class="space" v-show="this.shows.five">跳过<i class="el-icon-right"></i></router-link>
                    </transition>
                </div>
            </el-footer>
        </el-container>

    </div>
</template>

<script>
    export default {
        name: "WelcomePage",
        data() {
            return{
                shows: {
                    one: null,
                    two: null,
                    three: null,
                    four: null,
                    five:null
                }
            }
        },
        methods: {
            showTime(index){
                this.shows[index] = 1;
            },

            showByTime(){
                // let that = this;
                setTimeout(()=>{
                    this.shows.one =1;
                }, 1000);
                setTimeout(()=>{
                    this.shows.five =1;
                }, 2000);
                setTimeout(()=>{
                    this.shows.two =1;
                }, 3000);
                setTimeout(()=>{
                    this.shows.three =1;
                },5000);
                setTimeout(()=>{
                    this.shows.four =1;
                },7000);
            }
        },
        mounted() {
            this.showByTime();
        }
    }
</script>

<style scoped>
    p{
        text-align: left;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity 1.5s;
    }
    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
        opacity: 0;
    }

    #welcomePage{


    }

    .el-footer {
        color: #333;
        text-align: center;
        line-height: 8vm;
        height: 20% !important;
    }

    #footSpace{
        box-sizing: border-box;
        padding: 10% 5% 10% 10%;
        float: right;
        font-size: 6vw;
    }

    .el-main {
        box-sizing: border-box;
        color: #333;
        text-align: center;
        line-height: 20vw;
        height: 80%;
        padding: 15% 10% 10%;
        font-size: 8vw;
    }

    .el-container{
        height: 100%;
    }

    .space{
        text-decoration: none;
        color: black;
    }
</style>