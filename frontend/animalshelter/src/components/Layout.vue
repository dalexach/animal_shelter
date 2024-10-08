<template>
  <div class="layout">
    <NavBar />
    <main class="container mx-auto mt-8 px-4">
      <slot></slot>
    </main>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'Layout',
  components: {
    NavBar
  }
}
</script>