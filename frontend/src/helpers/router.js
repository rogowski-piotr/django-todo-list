import { createRouter, createWebHistory } from 'vue-router';
import Login from '../pages/Login.vue';
import Dashboard from '../pages/Dashboard.vue';
import AddTaks from '../pages/AddTaks.vue';
import ShowTask from '../pages/ShowTask.vue';
import Admin from '../pages/Admin.vue';
import Register from '../pages/Register.vue';


const routes = [
    { path: '/login', component: Login },
    { path: '/rejestracja', component: Register },
    { path: '/dodaj', component: AddTaks },
    { path: '/zadanie/:id', component: ShowTask },
    { path: '/', component: Dashboard },
    { path: '/admin', component: Admin },
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
    const publicPages = ['/login', '/rejestracja'];
    const adminPages = [ '/admin' ];
    const authRequired = !publicPages.includes(to.path);
    const adminRequired = adminPages.includes(to.path);
    const loggedIn = JSON.parse(localStorage.getItem('user'));
  
    // if you are not authenticated redirect to /login
    if (authRequired && !loggedIn) {
      console.log('redirecting to /login');
      return next({ 
        path: '/login', 
        query: { returnUrl: to.path } 
      });
    }

    // If you don't have admin role don't allow to go on adminPages
    if (adminRequired && !loggedIn.is_admin) {
      console.log('redirecting to /');
      return next({ 
        path: '/'
      });
    }

    // If you have admin role then allow only adminPages and logout (/login)
    if (!adminRequired && authRequired && loggedIn.is_admin) {
      console.log('redirecting to /admin');
      return next({ 
        path: '/admin'
      });
    }
  
    next();
})

export default router;