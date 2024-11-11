<script setup>
import { inject } from 'vue'
import Header from '../components/templates/Header.vue'

// apply theme style
const theme = inject("theme")
theme.apply()
</script>
<template>
  <main>
    <Header />
    <h1>about page</h1>
  </main>
</template>
