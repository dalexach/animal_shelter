<template>
  <div v-if="animal" class="animal-details">
    <h2 class="page-title">Detalles del Animal</h2>
    <div class="details-card">
      <p><strong>Nombre:</strong> {{ animal.nombre }}</p>
      <p><strong>Especie:</strong> {{ animal.especie }}</p>
      <p><strong>Raza:</strong> {{ animal.raza }}</p>
      <p><strong>Edad:</strong> {{ animal.edad }}</p>
      <p><strong>Peso:</strong> {{ animal.peso }} kg</p>
      <p><strong>Altura:</strong> {{ animal.altura }} cm</p>
      <p><strong>Sexo:</strong> {{ animal.sexo === 'M' ? 'Macho' : 'Hembra' }}</p>
    </div>
    <div class="button-group">
      <button @click="editAnimal" class="btn btn-primary">Editar</button>
      <button @click="deleteAnimal" class="btn btn-danger">Eliminar</button>
    </div>
  </div>
  <div v-else class="loading">Cargando...</div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import HealthRecord from './HealthRecord.vue'

export default {
  name: 'AnimalDetails',
  components: {
    HealthRecord
  },
  props: {
    id: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const animal = ref(null)

    const fetchAnimalDetails = async () => {
      try {
        const response = await axios.get(`https://animalshelter-27633f1524c4.herokuapp.com/api/animales/${props.id}/`)
        animal.value = response.data
      } catch (error) {
        console.error('Error fetching animal details:', error)
      }
    }

    onMounted(fetchAnimalDetails)

    return {
      animal
    }
  }
}
</script>

<style scoped>
.animal-details {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.page-title {
  font-size: 2rem;
  color: #2c5282;
  margin-bottom: 1.5rem;
  text-align: center;
}

.details-card {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 1.5rem;
}

.details-card p {
  margin-bottom: 0.5rem;
  color: #4a5568;
}

.details-card strong {
  color: #2c5282;
}

.button-group {
  display: flex;
  justify-content: space-between;
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
  cursor: pointer;
}

.btn-primary {
  background-color: #3490dc;
  color: white;
  border: none;
}

.btn-primary:hover {
  background-color: #2779bd;
}

.btn-danger {
  background-color: #e53e3e;
  color: white;
  border: none;
}

.btn-danger:hover {
  background-color: #c53030;
}

.loading {
  text-align: center;
  color: #4a5568;
  font-size: 1.2rem;
}
</style>