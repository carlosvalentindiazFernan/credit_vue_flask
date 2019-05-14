import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/components/Login'
import Credit from '@/components/Credit'
import List from '@/components/Lists'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/create',
      name: 'create',
      component: Credit      
    },
    {
      path: '/list',
      name: 'list',
      component: Lists              
    }

  ]
})
