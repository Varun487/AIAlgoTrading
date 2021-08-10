import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "LandingPage",
    component: () => import("../views/LandingPage.vue"),
  },
  {
    path: "/login",
    name: "Login",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/Login.vue"),
  },
  {
    path: '/allstrategies',
      name: 'AllStrategies',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AllStrategies.vue')
  },
  {
    path: "/strategy",
    name: "StrategyPage",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/StrategyPage.vue"),
  },
  {
    path: "/backtestreport",
    name: "BacktestReport",
    component: () => import("../views/BacktestReport.vue"),
  },
  {
    path: "/papertrades",
    name: "Papertrades",
    component: () => import("../views/Papertrades.vue"),
  },
  {
    path: "/apidocs",
    name: "APIDocs",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/RestApiDocs.vue"),
  },

  //<---------------------------------------Version 1 Code--------------------------------------->

  {
    path: '/strategiesv1',
      name: 'Strategies',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Strategies.vue')
  },
  {
    path: "/backtestv1",
    name: "Backtest",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("../views/Backtest.vue"),
  },
  {
    path: '/papertraderv1',
      name: 'Papertrader',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Papertrader.vue')
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
