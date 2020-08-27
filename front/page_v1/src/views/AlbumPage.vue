<!--相册页-->
<template>
    <div id="albumPage">
        <!--目前留出6个相册槽位，以后再加自动分页功能-->
        <div id="albumBlocks">
            <div class="albumBlock">
                <Album :number="0" :image-titles="albumTitles.one" :album-name="'七月'" :link-base="'personal-page-tan.oss-cn-beijing.aliyuncs.com/projects/personal_site/albums/july/file.csv'"/>
            </div>
            <div class="albumBlock">
            </div>
            <div class="albumBlock">
            </div>
            <div class="albumBlock">
            </div>
            <div class="albumBlock">
            </div>
            <div class="albumBlock">
            </div>
        </div>
        <!--分页导航，目前空出-->
        <div id="albumNavi">

        </div>
    </div>
</template>

<script>
    import Album from "../components/Album";
    export default {
        name: "AlbumPage",
        data() {
            return {
                albumTitles:{
                    /*后面会把这些照片名称也存在oss*/
                    one:[
                        '西贝莜面村',
                        '隐炙炭火烤肉',
                        '骑车载🐳',
                        '鸡公煲',
                        '和🐳在海洋馆',
                        '海底捞',
                        '海底捞2',
                        '南京夫子庙',
                        '柴🐶',
                        '柴🐶2'
                    ]
                }
            }
        },
        components: {Album}
    }
</script>

<style scoped>
    #albumPage{
        line-height: 0;
        height: 100%;
    }

    #albumBlocks{
        height: 85%;
        box-sizing: border-box;
    }

    #albumNavi{
        height: 15%;
    }

    div.albumBlock{
        box-sizing: border-box;
        padding: 3px;
        width: 33.3%;
        height: 50%;
        float: left;
    }


</style>