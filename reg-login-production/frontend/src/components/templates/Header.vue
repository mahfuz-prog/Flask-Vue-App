<script setup>
import axios from 'axios'
import { ref, inject, watch } from 'vue'
import { RouterView } from 'vue-router'
import { redirectNotify } from '../composables/handleAuthorization'

// this will handle all the logic for redirect and notification
const redirect = new redirectNotify()
const store = inject("store")

const isLogedIn = ref(false)

// this will watch every time the jwt token
// if /login-check in main.js return an error reset will reset and this will triggered
watch(store.state, (state) => {
  if (state.token === null) {
    isLogedIn.value = false
  }
})


if (store.state.token) {
  isLogedIn.value = true
} else {
  isLogedIn.value = false
}


// log out functionality
function logOut() {
  store.resetState()
  redirect.update('/', { title: 'Successfuly Signed Out', text: 'Now you have Limited access.' })
  redirect.use()
}
</script>
<template>
  <header>
    <div>
      <RouterLink to="/"><img alt="Site logo" class="logo" src="@/assets/logo.png" /></RouterLink>
    </div>
    <div class="wrapper">
      <nav v-if="isLogedIn">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/account">Account</RouterLink>
        <button @click="logOut">Log Out</button>
        <RouterView />
      </nav>
      <nav v-if="!isLogedIn">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/sign-up">Sign Up</RouterLink>
        <RouterLink to="/log-in">Log In</RouterLink>
      </nav>
    </div>
  </header>
</template>

<style scoped>
header {
  height: 65px;
  padding: 10px 10px 10px 10px;
  width: 1140px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: var(--secondary-black);
}

nav {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 30px;
}

.logo {
  width: 220px;
}

.router-link-active {
  color: var(--accent);
}

img {
  margin-bottom: -6px;
}

button {
  background-color: var(--accent);
  border: 0;
  padding: 8px 35px 8px 35px;
  border-radius: 25px;
  color: #ffffff;
  cursor: pointer;
}

@media (min-width: 768px) {
  header {
    padding: 10px 20px 10px 20px;
    width: 100%;
  }
}
</style>
