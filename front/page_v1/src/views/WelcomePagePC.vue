<!--PC端欢迎页面-->
<template>
    <div id="welcomePage_pc">
        <el-container>
            <el-main>
                <div id="lyrics">
                    <transition-group name="fade" tag="p">
                        <p :key="0" v-if="shows.one">Look</p>
                        <p :key="1" v-if="shows.two">If you had one shot, or one opportunity</p>
                        <p :key="2" v-if="shows.three">To seize everything you ever wanted</p>
                        <p :key="3" v-if="shows.four">One moment</p>
                        <p :key="4" v-if="shows.five">Would you capture it or just let it slip?</p>
                        <p class="quotation" :key="5" v-if="shows.six">-- Lose Yourself by Eminem</p>
                    </transition-group>
                </div>
            </el-main>
            <el-footer>
                <transition name="fade">
                    <router-link to="/main" id="go" v-if="shows.seven">
                        GO !
                    </router-link>
                </transition>
            </el-footer>
        </el-container>

    </div>
</template>

<script>
    export default {
        name: "WelcomePagePC",
        data() {
            return{
                shows: {
                    one: 0,
                    two: 0,
                    three: 0,
                    four: 0,
                    five: 0,
                    six: 0,
                    seven: 0,
                }
            }
        },

        methods: {
            showsByTime(){
                setTimeout(()=>{
                    this.shows.one =1;
                }, 1000);
                setTimeout(()=>{
                    this.shows.two =1;
                    this.shows.seven =1;
                }, 3000);
                setTimeout(()=>{
                    this.shows.three =1;
                }, 5000);
                setTimeout(()=>{
                    this.shows.four =1;
                },7000);
                setTimeout(()=>{
                    this.shows.five =1;
                },9000);
                setTimeout(()=>{
                    this.shows.six =1;
                },11000);
            }
        },

        mounted() {
            this.showsByTime()
        }
    }
</script>

<style scoped>

    .el-container{
        height: 100%;
    }

    .el-main{
        line-height: 80px;
    }

    .el-footer {

    }

    #lyrics{
        box-sizing: border-box;
        text-align: left;
        padding: 10vw;
        color: white;
        font-size: 2.2vw;
        font-weight: bold;
        font-family: Courier;
        text-transform: uppercase;
    }


    p.quotation{
        text-align: right;
    }

    #go{
        font-size: 20px;
        text-decoration: none;
        color: white;
        font-weight: bold;
    }

    #welcomePage_pc{
        background: url("https://personal-page-tan.oss-cn-beijing.aliyuncs.com/imgs/sea.jpg");
        background-size: 100% 100%;
    }

    .fade-enter-active{
        transition: all 1.5s ease;
    }
    .fade-enter{
        transform: translateX(10px);
        opacity: 0;
    }
</style>