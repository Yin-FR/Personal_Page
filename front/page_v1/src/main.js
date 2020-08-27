import Vue from 'vue';
import App from './App.vue';
import router from "./router";
import Vuex from 'vuex';
import store from './store';
import axios from 'axios';
import VueAxios from "vue-axios";

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import Viewer from "v-viewer";
import 'viewerjs/dist/viewer.css'

import vueAudioNative from 'vue-audio-native';

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
