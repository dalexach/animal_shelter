<template>
  <div class="animal-list">
    <h2>Lista de Animales</h2>
    <div v-if="loading">Cargando...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else class="animal-grid">
      <div v-for="animal in animals" :key="animal.id" class="animal-card">
        <h3>{{ animal.nombre }}</h3>
        <p>Especie: {{ animal.especie }}</p>
        <p>Hábitat: {{ animal.habitat }}</p>
        <router-link :to="{ name: 'AnimalDetails', params: { id: animal.id } }" class="btn-details">
          Ver detalles
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'AnimalList',
  setup() {
    const animals = ref([])
    const loading = ref(true)
    const error = ref(null)

    const fetchAnimals = async () => {
      try {
        const response = await axios.get('https://animalshelter-27633f1524c4.herokuapp.com/api/animales/')
        animals.value = response.data
        loading.value = false
      } catch (e) {
        error.value = 'Error al cargar los animales'
        loading.value = false
      }
    }

    onMounted(fetchAnimals)

    return {
      animals,
      loading,
      error
    }
  }
}
</script>

<style scoped>
.animal-list {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.animal-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

.animal-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  background-color: #f9f9f9;
}

.btn-details {
  display: inline-block;
  margin-top: 10px;
  padding: 5px 10px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 4px;
}
</style>