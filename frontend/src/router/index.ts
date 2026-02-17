import { createRouter, createWebHistory } from "vue-router";
import LandingView from "../views/LandingView.vue";
import LoginView from "../views/LoginView.vue";
import DashboardLayout from "../views/manager/DashboardLayout.vue";
import ServiceFormView from "../views/manager/ServiceFormView.vue";
import ServiceListView from "../views/manager/ServiceListView.vue";
import SpaceView from "../views/SpaceView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: LandingView,
  },
  {
    path: "/espaco",
    name: "space",
    component: SpaceView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/manager",
    component: DashboardLayout,
    meta: { requiresAuth: true },
    children: [
      {
        path: "",
        name: "dashboard",
        component: ServiceListView,
      },
      {
        path: "services/new",
        name: "service-new",
        component: ServiceFormView,
      },
      {
        path: "services/:id/edit",
        name: "service-edit",
        component: ServiceFormView,
        props: true,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, _from, next) => {
  const token = localStorage.getItem("token");
  if (to.meta.requiresAuth && !token) {
    next({ name: "login" });
  } else {
    next();
  }
});

export default router;
