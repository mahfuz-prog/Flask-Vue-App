<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'

const telegram = window.Telegram.WebApp
const router = useRouter()
  // BackButton functionality on telegram webapp window header
telegram.BackButton.onClick(() => {
  router.go(-1)
})
</script>
<template>
  <RouterLink to="/">
    <span>Home</span>
  </RouterLink>
  <RouterLink to="/about">
    <span>About</span>
  </RouterLink>
  <RouterView />
</template>

<style scoped>
</style>
