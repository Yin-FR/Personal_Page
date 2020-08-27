import Vue from 'vue';
import App from './App.vue';
import router from "./router"; /*路由*/
import Vuex from 'vuex'; /*管理全局仓库*/
import store from './store'; /*定义在./store目录下的全局仓库*/
import axios from 'axios'; /*网络请求*/
import VueAxios from "vue-axios"; /*网络请求*/

import ElementUI from 'element-ui'; /*element-ui库*/
import 'element-ui/lib/theme-chalk/index.css'; /*对应css文件*/

//链接： https://github.com/mirari/v-viewer
import Viewer from "v-viewer"; /*相册详细功能库*/
import 'viewerjs/dist/viewer.css' /*对应css文件*/

import vueAudioNative from 'vue-audio-native'; /*音乐播放器插件*/

Vue.config.productionTip = false;

Vue.use(VueAxios, axios)
Vue.use(Vuex);
Vue.use(ElementUI);
Vue.use(Viewer);
Vue.use(vueAudioNative)


new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app')
