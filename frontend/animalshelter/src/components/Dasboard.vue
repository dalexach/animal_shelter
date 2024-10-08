<template>
  <div class="dashboard">
    <h1>Panel de Control</h1>
    <nav>
      <router-link to="/animals">Gestionar Animales</router-link>
      <router-link to="/caregivers">Gestionar Cuidadores</router-link>
      <router-link to="/reports">Reportes</router-link>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Dashboard'
}
</script>

<style scoped>
.dashboard {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

nav {
  display: flex;
  justify-content: space-around;
  margin-top: 20px;
}

a {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}

a:hover {
  background-color: #45a049;
}
</style>