<script setup>
import { inject } from 'vue'

// apply theme style
const theme = inject("theme")
theme.apply()
</script>
<template>
  <main>
    <h1>about page</h1>
  </main>
</template>
