<script setup>
defineProps({
  err: String
})
</script>
<template>
  <main>
    <i><h1>{{ err }}</h1></i>
  </main>
</template>

<style scoped>
main {
  /*  full height - header height and footer height*/
  height: calc(100vh - 65px - 42px);
  display: grid;
  place-items: center;
}

h1 {
  font-weight: 700;
}
</style>
