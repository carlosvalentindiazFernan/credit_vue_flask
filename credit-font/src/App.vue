<template>
  <div class="page-container">
    <md-app md-mode="reveal">
      <md-app-toolbar class="md-primary">
        <template v-if="isLogin">
          <md-button class="md-icon-button" @click="menuVisible = !menuVisible">
            <md-icon>menu</md-icon>
          </md-button>
        </template>
        <span class="md-title">My Title</span>
      </md-app-toolbar>

      <md-app-drawer :md-active.sync="menuVisible">
        <md-toolbar class="md-transparent" md-elevation="0">Navigation</md-toolbar>

        <md-list>
          <md-list-item>
            <md-icon>move_to_inbox</md-icon>
            <span class="md-list-item-text"
              @click="listCredit">
              List Credit
            </span>
          </md-list-item>

          <md-list-item>
            <md-icon>send</md-icon>
            <span class="md-list-item-text"
              @click="createCredit">
              Create Credit
            </span>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content>
        <Login v-on:event="onLogin"></Login>
      </md-app-content>
    </md-app>
  </div>
</template>

<style scoped>
  .md-app {
    max-height: 400px;
    border: 1px solid rgba(#000, .12);
  }

   // Demo purposes only
  .md-drawer {
    width: 230px;
    max-width: calc(100vw - 125px);
  }
</style>

<script>
import Login from './components/Login'
export default {
  name: 'App',
  components: {
    Login
  },
  data: () => ({
    menuVisible: false,
    isLogin: false,
    auth: null
  }),
  methods: {
    onLogin (e) {
      this.isLogin = e.isLogin
      if (e.isLogin) {
        this.auth = e.token
      }
    },
    createCredit () {
      console.log('create credit')
    },
    listCredit () {
      console.log('list credit')
    }
  }
}
</script>
