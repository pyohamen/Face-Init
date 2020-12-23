import LoginLayout from "@/layout/login/LoginLayout.vue"
import MainLayout from "@/layout/main/MainLayout.vue"
// GeneralViews
import NotFound from "@/pages/NotFoundPage.vue";

import axios from 'axios'

// Pages
const WorkerTable = () => import("@/pages/WorkerTable.vue")
const MainPage = () => import("@/pages/MainPage.vue")


// 접근 제한
const resourceHost = 'http://i3a207.p.ssafy.io:8000'

const requireAuth = () => (from, to, next) => {
    if (localStorage.getItem('accessToken') == null) {
        return next('/login')
    }
    axios.get(`${resourceHost}/login/`).then(({ data }) => {
        if (data.message === undefined) {
            next('/login')
        } else {
            return next()
        }
    })
}

const haveAuth = () => (from, to, next) => {
    if (localStorage.getItem('accessToken') != null) {
        return next('/')
    }
    return next()
}


const routes = [
    { path: "*", component: NotFound },
    {
        path: "/login",
        component: LoginLayout,
        name: "login",
        beforeEnter: haveAuth()
    },
    {
        path: "/",
        component: MainLayout,
        redirect: "/home",
        beforeEnter: requireAuth(),
        children: [
            {
                path: "home",
                name: "home",
                component: MainPage
            },
            {
                path: "management",
                name: "management",
                component: WorkerTable
            },
        ]
    },
];

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/

export default routes;
