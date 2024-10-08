<template>
  <div class="home">
    <h1 class="page-title">Bienvenido al Sistema de Gestión de Refugio de Animales</h1>
    <div class="card-grid">
      <div class="card">
        <h2 class="card-title">Animales</h2>
        <p class="card-text">Gestiona los animales en el refugio.</p>
        <div class="card-actions">
          <router-link to="/animals" class="btn btn-primary">Ver Animales</router-link>
          <router-link to="/add-animal" class="btn btn-secondary">Agregar Animal</router-link>
        </div>
      </div>
      <div class="card">
        <h2 class="card-title">Cuidadores</h2>
        <p class="card-text">Administra los cuidadores del refugio.</p>
        <div class="card-actions">
          <router-link to="/caregivers" class="btn btn-primary">Ver Cuidadores</router-link>
          <router-link to="/add-caregiver" class="btn btn-secondary">Agregar Cuidador</router-link>
        </div>
      </div>
      <div class="card">
        <h2 class="card-title">Reportes</h2>
        <p class="card-text">Accede a los reportes del refugio.</p>
        <router-link to="/reports" class="btn btn-primary">Ver Reportes</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.page-title {
  font-size: 2rem;
  font-weight: bold;
  color: #2c5282;
  margin-bottom: 1.5rem;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.card {
  background-color: white;
  padding: 1.5rem;
  border-radius: 0.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card-title {
  font-size: 1.25rem;
  font-weight: bold;
  color: #2c5282;
  margin-bottom: 0.75rem;
}

.card-text {
  color: #4a5568;
  margin-bottom: 1rem;
}

.card-actions {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
</style>