//路由配置文件
import Vue from 'vue';
import Router from 'vue-router';

import WelcomePage from "./views/WelcomePage";
import MainPage from "./views/MainPage";
import WelcomePagePC from "./views/WelcomePagePC";
import HomePage from "./views/HomePage";
import ProjectPage from "./views/ProjectPage";
import DairyPage from "./views/DairyPage";
import CommentPage from "./views/CommentPage";

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes:[
        {path: '/welcome', name:'welcome', component: WelcomePagePC},
        {path: '/welcomeM', name: 'welcomeM', component: WelcomePage},
        {
            path: '/main',
            name: 'main',
            component: MainPage,
            children: [
                {path: 'home', name: 'home', component: HomePage},
                {path: 'album', name: 'album', component: resolve => (require(['./views/AlbumPage'], resolve))}, /*这一路由静态资源请求较多，所以配置懒加载*/
                {path: 'dairy', name: 'dairy', component: DairyPage},
                {path: 'project', name: 'project', component: ProjectPage},
                {path: 'comment', name: 'comment', component: CommentPage},
            ],
            redirect: '/main/home'}
    ]
})