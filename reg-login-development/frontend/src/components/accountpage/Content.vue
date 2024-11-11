<script setup>
import { ref } from 'vue'
import { loginRequired } from '../composables/handleAuthorization'

// this function fetch data and return data for login-required route
const status = new loginRequired('account/')
const data = await status.check()

const username = ref()
const email = ref()

if (data) {
  username.value = data.name
  email.value = data.email
} else {}
</script>
<template>
  <div>
    <h4><span>Username: </span>{{ username }}</h4>
    <h4><span>Email: </span>{{ email }}</h4>
  </div>
</template>

<style scoped>
span {
  color: #ffffff;
}
</style>
