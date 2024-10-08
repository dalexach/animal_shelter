<template>
  <Layout>
    <router-view></router-view>
  </Layout>
</template>

<script>
import Layout from '@/components/Layout.vue'

export default {
  name: 'App',
  components: {
    Layout
  }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  background-color: #f0f8ff; /* Azul claro */
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.btn {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.btn-primary {
  background-color: #3490dc;
  color: white;
}

.btn-primary:hover {
  background-color: #2779bd;
}

.btn-secondary {
  background-color: #6cb2eb;
  color: white;
}

.btn-secondary:hover {
  background-color: #4e9ae1;
}
</style>