<template>
  <div class="animal-details" v-if="animal">
    <h2>{{ animal.nombre }}</h2>
    <div class="details-grid">
      <div>
        <p><strong>Especie:</strong> {{ animal.especie }}</p>
        <p><strong>Hábitat:</strong> {{ animal.habitat }}</p>
        <p><strong>Tipo de Comida:</strong> {{ animal.tipo_comida }}</p>
        <p><strong>Marca de Comida:</strong> {{ animal.marca_comida }}</p>
      </div>
      <div>
        <h3>Necesidades de Aseo</h3>
        <p>{{ animal.necesidades_aseo }}</p>
        <h3>Necesidades de Aseo del Hábitat</h3>
        <p>{{ animal.necesidades_aseo_habitat }}</p>
      </div>
    </div>
    <HealthRecord :animalId="animal.id" />
  </div>
  <div v-else>Cargando detalles del animal...</div>
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
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.details-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

h3 {
  margin-top: 20px;
}
</style>