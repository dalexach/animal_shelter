<template>
  <div class="home">
    <h1>Bienvenido al Refugio de Animales</h1>
    <p>Aquí puedes gestionar los animales, cuidadores y reportes del refugio.</p>
    <Dashboard />
  </div>
</template>

<script>
import Dashboard from '@/components/Dashboard.vue'

export default {
  name: 'Home',
  components: {
    Dashboard
  }
}
</script>

<style scoped>
.home {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}
</style>