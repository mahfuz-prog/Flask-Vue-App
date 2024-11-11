import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'
import AccountView from '../views/AccountView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/sign-up',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/log-in',
      name: 'login',
      component: LogInView
    },
    {
      path: '/account',
      name: 'account',
      component: AccountView
    },
  ]
})

export default router
