<script setup>
import Header from '../components/templates/Header.vue'
import Footer from '../components/templates/Footer.vue'
import Content from '../components/signuppage/Content.vue'

import { inject } from 'vue'
import { redirectNotify } from '../components/composables/handleAuthorization'

// reactive store object
const store = inject("store")

// this will handle all the logic for redirect and notification
const redirect = new redirectNotify()


if (store.state.token) {
  // first arguments is route and second one is a object containing title, text
  redirect.update('/', { title: 'Sign Up Not Allowed', text: 'You already have an account' })
  redirect.use()
}
</script>
<template>
  <Header />
  <main>
    <Content />
  </main>
  <Footer />
</template>

<style scoped>
main {
  height: calc(100vh - 65px - 42px);
  display: grid;
  place-items: center;
}
</style>
