<script setup>
import { RouterView, useRouter } from 'vue-router'

const telegram = window.Telegram.WebApp
const router = useRouter()
  // BackButton functionality on telegram webapp window header
telegram.BackButton.onClick(() => {
  router.go(-1)
})
</script>
<template>
  <RouterView />
</template>

<style scoped>
</style>
