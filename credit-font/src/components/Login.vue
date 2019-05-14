<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Login</h2>
    <section>
      <form novalidate class="md-layout">
          <md-card class="md-layout-item md-size-50 md-small-size-100">

            <md-card-content>
              <md-field>
                <label for="email">Email</label>
                <md-input type="email"
                  name="email"
                  id="email"
                  v-model="auth.email"
                  autocomplete="email"  />
                <span class="md-error">The email is required</span>
                <span class="md-error">Invalid email</span>
              </md-field>
              <md-field>
                <label for="password">Password</label>
                <md-input type="password"
                  name="password"
                  id="password"
                  v-model="auth.password"
                  autocomplete="password"  />
                <span class="md-error">The password is required</span>
                <span class="md-error">Invalid password</span>
              </md-field>
            </md-card-content>

            <md-card-actions>
              <md-button class="md-raised md-primary"
                @click="eventLogin">
                Primary
              </md-button>
            </md-card-actions>
          </md-card>

        </form>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      auth: {
        email: null,
        password: null
      }
    }
  },
  methods: {
    eventLogin () {

      axios.post('http://127.0.0.1:5000/api/v1/login/', this.auth)
      .then((response) => {
        let value = {
          isLogin: true,
          token: response.data
        }
        this.msg = 'Welcome to Your Vue.js App'
        this.$emit('event', value)
      })
      .catch((error) =>{
        this.msg = error
        let value = {
          isLogin: false,
          token: ''
        }
        this.$emit('event', value)
      });



    }
  }
}
</script>
