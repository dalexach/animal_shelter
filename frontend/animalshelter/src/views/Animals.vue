<template>
  <div class="animals-view">
    <h1 class="page-title">Listado de Animales</h1>
    <router-link to="/add-animal" class="btn btn-primary mb-4">Agregar Animal</router-link>
    <div class="animal-grid">
      <div v-for="animal in animals" :key="animal.id" class="animal-card">
        <h2 class="animal-name">{{ animal.nombre }}</h2>
        <p><strong>Especie:</strong> {{ animal.especie }}</p>
        <p><strong>Edad:</strong> {{ animal.edad }} años</p>
        <router-link :to="{ name: 'AnimalDetails', params: { id: animal.id } }" class="btn btn-secondary">Ver Detalles</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import AnimalList from '@/components/AnimalList.vue'

export default {
  name: 'Animals',
  components: {
    AnimalList
  }
}
</script>

<style scoped>
.animals-view {
  padding: 20px;
}

.page-title {
  font-size: 2rem;
  color: #2c5282;
  margin-bottom: 1.5rem;
  text-align: center;
}

.btn {
  display: inline-block;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  border-radius: 4px;
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

.mb-4 {
  margin-bottom: 1rem;
}

.animal-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

.animal-card {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.animal-name {
  font-size: 1.25rem;
  color: #2c5282;
  margin-bottom: 0.5rem;
}

.animal-card p {
  margin-bottom: 0.5rem;
  color: #4a5568;
}
</style>