<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Credit-Create</h2>
    <section>
        <p>Credits</p>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Credit',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      auth: {
        email: null,
        password: null
      }
    }
  }
}
</script>
