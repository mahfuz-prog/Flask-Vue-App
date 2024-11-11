<script setup>
import { onErrorCaptured, ref } from 'vue'
import Header from '../components/templates/Header.vue'
import Footer from '../components/templates/Footer.vue'
import Error from '../components/templates/Error.vue'
import Content from '../components/homepage/Content.vue'
import ContentSkeleton from '../components/homepage/ContentSkeleton.vue'

const error = ref(false)

onErrorCaptured((err) => {
  error.value = true
})
</script>
<template>
  <Header />
  <main v-if="!error">
    <Suspense>
      <template #default>
        <Content />
      </template>
      <template #fallback>
        <ContentSkeleton />
      </template>
    </Suspense>
  </main>
  <Error err="404" v-if="error" />
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
