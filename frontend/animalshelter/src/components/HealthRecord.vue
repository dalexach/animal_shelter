<template>
  <div class="health-record">
    <h3>Registros de Salud</h3>
    <div v-if="loading">Cargando registros de salud...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
      <ul>
        <li v-for="record in healthRecords" :key="record.id">
          <strong>{{ record.tipo }}</strong> - {{ formatDate(record.fecha) }}
          <p>{{ record.descripcion }}</p>
        </li>
      </ul>
    </div>
    <button @click="showAddForm = true">Añadir Registro de Salud</button>
    <AddHealthRecord
      v-if="showAddForm"
      :animalId="animalId"
      @recordAdded="fetchHealthRecords"
      @cancel="showAddForm = false"
    />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import AddHealthRecord from './AddHealthRecord.vue'

export default {
  name: 'HealthRecord',
  components: {
    AddHealthRecord
  },
  props: {
    animalId: {
      type: Number,
      required: true
    }
  },
  setup(props) {
    const healthRecords = ref([])
    const loading = ref(true)
    const error = ref(null)
    const showAddForm = ref(false)

    const fetchHealthRecords = async () => {
      try {
        const response = await axios.get(`https://animalshelter-27633f1524c4.herokuapp.com/api/registros-salud/?animal=${props.animalId}`)
        healthRecords.value = response.data
        loading.value = false
      } catch (e) {
        error.value = 'Error al cargar los registros de salud'
        loading.value = false
      }
    }

    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString()
    }

    onMounted(fetchHealthRecords)

    return {
      healthRecords,
      loading,
      error,
      showAddForm,
      fetchHealthRecords,
      formatDate
    }
  }
}
</script>

<style scoped>
.health-record {
  margin-top: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 15px;
  border-bottom: 1px solid #ddd;
  padding-bottom: 10px;
}

button {
  margin-top: 10px;
  padding: 5px 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}
</style>