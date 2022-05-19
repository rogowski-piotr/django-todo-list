import { createRouter, createWebHistory } from 'vue-router';
import Login from '../pages/Login.vue';
import Dashboard from '../pages/Dashboard.vue';
import AddTaks from '../pages/AddTaks.vue';


const routes = [
    { path: '/login', component: Login },
    { path: '/dodaj', component: AddTaks },
    { path: '/', component: Dashboard },
    {
      path: "/:catchAll(.*)",
      redirect: '/',
      meta: {
        requiresAuth: false
      }
    }
];


const router = createRouter({
    history: createWebHistory(),
    routes,
})


router.beforeEach((to, from, next) => {
    // redirect to login page if not logged in and trying to access a restricted page
    const publicPages = ['/login'/*, '/signup'*/];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('user');
  
    if (authRequired && !loggedIn) {
      return next({ 
        path: '/login', 
        query: { returnUrl: to.path } 
      });
    }
  
    next();
  })

export default router;