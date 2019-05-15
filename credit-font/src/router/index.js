import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Credit from '@/components/Credit'
import Lists from '@/components/Lists'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/credit',
      name: 'credit',
      component: Credit
    },
    {
      path: '/lists',
      name: 'lists',
      component: Lists
    }

  ]
})
