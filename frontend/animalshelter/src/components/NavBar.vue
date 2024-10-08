<template>
  <nav class="navbar">
    <div class="navbar-container">
      <router-link to="/" class="navbar-brand">Animal Shelter</router-link>
      <div class="navbar-links">
        <router-link to="/" class="navbar-link">Inicio</router-link>
        <router-link to="/animals" class="navbar-link">Animales</router-link>
        <router-link to="/caregivers" class="navbar-link">Cuidadores</router-link>
        <router-link to="/reports" class="navbar-link">Reportes</router-link>
        <button @click="logout" class="navbar-link">Cerrar Sesión</button>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  methods: {
    logout() {
      localStorage.removeItem('token')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.navbar {
  background-color: #e6f3ff;
  padding: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.navbar-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
}

.navbar-brand {
  color: #2c5282;
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
}

.navbar-links {
  display: flex;
  gap: 1rem;
}

.navbar-link {
  color: #4299e1;
  text-decoration: none;
  transition: color 0.3s ease;
}

.navbar-link:hover {
  color: #2b6cb0;
}
</style>