import Vue from 'vue';
import Router from 'vue-router';

import WelcomePage from "./views/WelcomePage";
import MainPage from "./views/MainPage";
import WelcomePagePC from "./views/WelcomePagePC";
import HomePage from "./views/HomePage";
import ProjectPage from "./views/ProjectPage";
import AlbumPage from "./views/AlbumPage";
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
                {path: 'album', name: 'album', component: AlbumPage},
                {path: 'dairy', name: 'dairy', component: DairyPage},
                {path: 'project', name: 'project', component: ProjectPage},
                {path: 'comment', name: 'comment', component: CommentPage},
            ],
            redirect: '/main/home'}
    ]
})