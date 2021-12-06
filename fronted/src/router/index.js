/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Poll from '@/components/Poll'
import Table from '@/components/Table'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/poll',
      name: 'Poll',
      component: Poll,
    },
    {
      path: '/table',
      name: 'Table',
      component: Table,
    }
  ],
  mode: 'history'
})
