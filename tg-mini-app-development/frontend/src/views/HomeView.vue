<script setup>
import { inject } from 'vue'
import Header from '../components/templates/Header.vue'
import Content from '../components/homepage/Content.vue'
import ContentSkeleton from '../components/homepage/ContentSkeleton.vue'

// apply theme style
const theme = inject("theme")
theme.apply()
</script>
<template>
  <Header />
  <main>
    <Suspense>
      <template #default>
        <Content />
      </template>
      <template #fallback>
        <ContentSkeleton />
      </template>
    </Suspense>
  </main>
</template>
