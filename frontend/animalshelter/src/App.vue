<template>
  <Layout>
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </Layout>
</template>

<script>
import { defineComponent, onMounted } from 'vue'
import { useStore } from 'vuex'
import Layout from '@/components/Layout.vue'

export default defineComponent({
  name: 'App',
  components: {
    Layout
  },
  setup() {
    const store = useStore()

    onMounted(() => {
      store.dispatch('checkAuth')
    })

    return {}
  }
})
</script>

<style>
:root {
  --primary-color: #3490dc;
  --primary-hover: #2779bd;
  --secondary-color: #6cb2eb;
  --secondary-hover: #4e9ae1;
  --background-color: #f0f8ff;
  --text-color: #2c3e50;
  --border-radius: 0.25rem;
}

body {
  margin: 0;
  padding: 0;
  font-family: 'Arial', sans-serif;
  background-color: var(--background-color);
  color: var(--text-color);
  line-height: 1.6;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.btn {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: var(--border-radius);
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  transition: background-color 0.3s ease, transform 0.2s ease;
  cursor: pointer;
  border: none;
}

.btn:hover {
  transform: translateY(-2px);
}

.btn-primary {
  background-color: var(--primary-color);
  color: white;
}

.btn-primary:hover {
  background-color: var(--primary-hover);
}

.btn-secondary {
  background-color: var(--secondary-color);
  color: white;
}

.btn-secondary:hover {
  background-color: var(--secondary-hover);
}

.card {
  background-color: white;
  border-radius: var(--border-radius);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1rem;
  margin-bottom: 1rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: var(--border-radius);
  font-size: 1rem;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>