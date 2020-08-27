<!--相册组件-->
<template>
    <div id="Album" style="height: 100%">
        <!--每个相册用卡片嵌套-->
        <el-card class="cardAlbum" style="height: 100%" body-style="padding: 0; height: 100%" :shadow="'always'">
            <!--卡片内内容-->
            <div id="AlbumInside" v-if="imageLinks" style="height: 100%">
                <!--相册封面跑马灯效果-->
                <el-carousel style="height: 80%; overflow: hidden" :indicator-position="'none'">
                    <!--选取3-5张作为封面轮播-->
                    <el-carousel-item v-for="(imageLink, index) in imageLinks.slice(3,6)" :key="imageLink" style="height: 100%; overflow: hidden">
                        <!--图片cover模式覆盖-->
                        <el-image :src="imageLink" :alt="imageLink" :fit="'cover'" style="height: 100%"/>
                    </el-carousel-item>
                </el-carousel>
                <!--点击区域-->
                <div id="clickArea">
                    <!--点击按钮调取v-viewer组件-->
                    <el-button id="intro" type="primary" plain @click="toShowViewer()">
                        <span>{{albumName}}</span>
                    </el-button>
                </div>
            </div>
        </el-card>
        <!--v-viewer用于详细的相册浏览功能组件-->
        <div class="images" v-viewer="{movable:false, interval: 3000}">
            <el-image v-for="(image, index) in imageLinks" :src="image" :key="image" :fit="'contain'" :alt="imageTitles[index]" v-show="false"/>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Album",
        props:{
            number: Number,
            linkBase: String,
            albumName: String,
            imageTitles: Array
        },
        data(){
            return{
                showViewer: 0,
                imageLinks:null,
                dialogVisible: false,
            }
        },
        methods: {
            /*打开v-viewer*/
            toShowViewer(){
                /*定位挂载在class为.images的v-viewer*/
                /*参考：https://github.com/mirari/v-viewer，https://mirari.cc/2017/08/27/Vue%E5%9B%BE%E7%89%87%E6%B5%8F%E8%A7%88%E7%BB%84%E4%BB%B6v-viewer%EF%BC%8C%E6%94%AF%E6%8C%81%E6%97%8B%E8%BD%AC%E3%80%81%E7%BC%A9%E6%94%BE%E3%80%81%E7%BF%BB%E8%BD%AC%E7%AD%89%E6%93%8D%E4%BD%9C/*/
                const viewer = this.$el.querySelector('.images').$viewer;
                /*展示*/
                viewer.show();
            },
            /*获取包含需要展示的图片的链接的array，以及需要的图片数量*/
            getImageLinks(index, linkImageBase){
                const axiosAjax = this.axios.create({
                    timeout: 60*1000,
                    withCredentials: true
                });
                let config = {
                    header: {
                        'Content-Type':'application/json'
                    },
                    params: {
                        link: linkImageBase,
                        index: index
                    }
                };
                axiosAjax.get('http://47.98.136.14:4100/communication/album', config).then((res)=>{
                    setTimeout(()=>{this.imageLinks = res.data;}, 100)

                }).catch((err)=>{
                    this.$notify({
                        type: 'error',
                        title: '获取相册数据出错',
                        message: '请刷新',
                    })
                });

            },
        },
        /*组件渲染完成即调用*/
        mounted() {
            this.getImageLinks(this.number, this.linkBase);
        }
    }
</script>

<style lang="scss">
    #Album{
        height: 100%;
        box-sizing: border-box;
        padding: 2vw;
    }

    .el-carousel__container{
        height: 100%;
    }

    #clickArea{
        height: 20%;
        text-align: center;
        position: relative;
    }

    #intro{
        height: 50%;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        margin: auto;
        padding: 0.2vw 2vw;
    }

    .cardAlbum{

    }

    .el-dialog__body{
        margin: 2vw;
    }

    .el-image{
        margin-bottom: 2vw;
    }
</style>