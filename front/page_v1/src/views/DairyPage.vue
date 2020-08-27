<template>
    <div id="dairyPage">
        <div class="block">
            <el-timeline>
                <el-timeline-item timestamp="2020/6" placement="top" type="success">
                    <el-card>
                        <h4>实习</h4>
                        <p><i class="el-icon-position"></i> 中国 合肥</p>
                    </el-card>
                </el-timeline-item>
                <el-timeline-item timestamp="2020/3" placement="top" type="primary">
                    <el-card style="margin-bottom: 10vw">
                        <h4>Gap year 回国</h4>
                        <p><i class="el-icon-position"></i> 中国 上海</p>
                    </el-card>
                </el-timeline-item>
                <el-timeline-item timestamp="2019/7" placement="top" type="primary">
                    <el-card style="margin-bottom: 40vw">
                        <h4>入读IMT Atlantique</h4>
                        <p><i class="el-icon-position"></i> 法国 布雷斯特</p>
                    </el-card>
                </el-timeline-item>
                <el-timeline-item timestamp="2015/9" placement="top" type="primary">
                    <el-card style="margin-bottom: 24vw">
                        <h4>入读西安电子科技大学</h4>
                        <p><i class="el-icon-position"></i> 中国 西安</p>
                    </el-card>
                </el-timeline-item>
                <el-timeline-item timestamp="2012/9" placement="top" type="primary">
                    <el-card style="margin-bottom: 24vw">
                        <h4>入读池州一中</h4>
                        <p><i class="el-icon-position"></i> 中国 池州</p>
                    </el-card>
                </el-timeline-item>
                <el-timeline-item timestamp="2009/9" placement="top" type="primary">
                    <el-card style="margin-bottom: 100vw">
                        <h4>入读池州十一中</h4>
                        <p><i class="el-icon-position"></i> 中国 池州</p>
                    </el-card>
                </el-timeline-item>
                <el-timeline-item timestamp="1998/6" placement="top" type="primary">
                    <el-card>
                        <h4>出生</h4>
                        <p><i class="el-icon-position"></i> 中国 池州</p>
                    </el-card>
                </el-timeline-item>
            </el-timeline>
        </div>
        <div id="contact">

        </div>
    </div>
</template>

<script>
    export default {
        name: "DairyPage"
    }
</script>

<style scoped>
    #dairyPage{
        line-height: 30px;
    }

    .block{
        padding: 6vw;
    }

    h4{
        font-size: 1.3em;
    }

    p{
        font-size: 1em;
    }

</style>