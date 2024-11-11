<script setup>
import { ref } from 'vue'
import axios from 'axios'
import DocumentationIcon from '../icons/IconDocumentation.vue'

const data = ref(await (await axios.get('/')).data)
</script>
<template>
  <div>
    <DocumentationIcon fill="red" />
    <h4>{{ data }}</h4>
  </div>
</template>

<style scoped>
div {
  width: 200px;
  height: 200px;
  border-radius: 10px;
  background-color: var(--secondary-black);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 10px;
}
</style>
