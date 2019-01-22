import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import actionDetail from './views/Detail.vue'
import New from './views/New.vue'
import Reply from './views/Message.vue'
import Pass from './views/Pass.vue'

Vue.use(Router)

const router = new Router({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/landing',
      name: 'landing',
      component: () => import(/* webpackChunkName: "about" */ './views/Landing.vue')
    },
    {
      path: '/detail/:aid',
      name: 'actionDetail',
      component: actionDetail,
    },
    {
      path: '/new',
      name: 'newActivity',
      component: New,
    },
    {
      path: '/message/:aid',
      name: 'messageReply',
      component: Reply,
    },
    {
      path: '/pass/:aid',
      name: 'passDetail',
      component: Pass
    },
    {
      path: '/personal/:page',
      name: 'personal',
      component: () => import(/* webpackChunkName: "about" */ './views/Personal.vue')
    }
  ]
})
// router.beforeEach((to, from, next) => {
//   // do something
//   console.log("to.path",to.path); 
//   console.log("form.path",from.path);

//   next();
// });
export default router