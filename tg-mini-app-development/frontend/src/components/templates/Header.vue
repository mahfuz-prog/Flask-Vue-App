<script setup>
import { RouterLink, RouterView } from 'vue-router'
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
