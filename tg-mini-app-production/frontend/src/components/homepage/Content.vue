<script setup>
import { ref } from 'vue'
import axios from 'axios'

const data = ref()

try {
  data.value = await (await axios.get('/')).data
  console.log(data.value)
} catch (err) {
  console.log(err.status)
}
</script>
<template>
  <main>
    <h1>{{ data }}</h1>
  </main>
</template>

<style scoped>
</style>
