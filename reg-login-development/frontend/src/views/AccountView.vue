<script setup>
import Header from '../components/templates/Header.vue'
import Footer from '../components/templates/Footer.vue'
import Content from '../components/accountpage/Content.vue'
</script>
<template>
  <Header />
  <main>
    <Suspense>
      <template #default>
        <Content/>
      </template>
      <template #fallback>
        <span>Loading...</span>
      </template>
    </Suspense>
  </main>
  <Footer />
</template>

<style scoped>
main {
  /*  full height - header height and footer height*/
  height: calc(100vh - 65px - 42px);
  display: grid;
  place-items: center;
}
</style>
