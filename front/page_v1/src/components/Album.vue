<template>
    <div id="Album" style="height: 100%">
        <el-card class="cardAlbum" style="height: 100%" body-style="padding: 0; height: 100%" :shadow="'always'">
            <div id="AlbumInside" v-if="imageLinks" style="height: 100%">
                <el-carousel style="height: 80%; overflow: hidden" :indicator-position="'none'">
                    <el-carousel-item v-for="(imageLink, index) in imageLinks.slice(3,6)" :key="imageLink" style="height: 100%; overflow: hidden">
                        <el-image :src="imageLink" :alt="imageLink" :fit="'cover'" style="height: 100%"/>
                    </el-carousel-item>
                </el-carousel>
                <div id="clickArea">
                    <el-button id="intro" type="primary" plain @click="toShowViewer()">
                        <span>{{albumName}}</span>
                    </el-button>
                </div>
            </div>
        </el-card>
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
            toShowViewer(){
                console.log('0')
                const viewer = this.$el.querySelector('.images').$viewer;
                viewer.show();
            },
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