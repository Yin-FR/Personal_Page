// 导入compression-webpack-plugin
const CompressionWebpackPlugin = require('compression-webpack-plugin');
// 定义压缩文件类型
const productionGzipExtensions = ['js', 'css']

// 没有配置太多东西，就加了一个项目打包时候对js和css压缩，提高服务器的加载速度
// 参考链接：https://blog.csdn.net/superKM/article/details/102627370
module.exports = {
    //统一配置打包插件
    configureWebpack: {
        plugins: [
            new CompressionWebpackPlugin({
                filename: '[path].gz[query]',
                algorithm: 'gzip',
                test: new RegExp('\\.(' + productionGzipExtensions.join('|') + ')$'),//匹配文件名
                threshold: 10240,//对10K以上的数据进行压缩
                minRatio: 0.8,
                deleteOriginalAssets:false,//是否删除源文件
            })
        ]
    },
}