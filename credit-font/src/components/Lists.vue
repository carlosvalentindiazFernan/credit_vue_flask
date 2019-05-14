<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Login</h2>
    <section>
        <p>Credits</p>
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
    eventList () {

      axios.get('http://127.0.0.1:5000/credits/', this.auth)
      .then((response) => {
        this.$emit('event', value)
      })
      .catch((error) =>{
        this.$emit('event', value)
      });


    }
  }
}
</script>
