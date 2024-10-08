<template>
  <div class="health-record">
    <h2 class="page-title">Registros de Salud</h2>
    <div v-if="loading" class="loading">Cargando registros de salud...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else>
      <div class="health-records-list">
        <div v-for="record in healthRecords" :key="record.id" class="health-record-card">
          <h3 class="record-title">{{ formatRecordType(record.tipo) }}</h3>
          <p class="record-date">Fecha: {{ formatDate(record.fecha) }}</p>
          <p class="record-description">{{ truncateDescription(record.descripcion) }}</p>
          <button @click="toggleFullDescription(record)" class="btn btn-secondary">
            {{ record.showFullDescription ? 'Ver menos' : 'Ver más' }}
          </button>
        </div>
      </div>
    </div>
    <button @click="showAddForm = true" class="btn btn-primary">Añadir Registro de Salud</button>
    <AddHealthRecord
      v-if="showAddForm"
      :animalId="animalId"
      @recordAdded="handleRecordAdded"
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
        healthRecords.value = response.data.map(record => ({
          ...record,
          showFullDescription: false
        }))
        loading.value = false
      } catch (e) {
        error.value = 'Error al cargar los registros de salud'
        loading.value = false
      }
    }

    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString()
    }

    const formatRecordType = (type) => {
      const types = {
        'vacuna': 'Vacuna',
        'examen': 'Examen',
        'tratamiento': 'Tratamiento'
      }
      return types[type] || type
    }

    const truncateDescription = (description, length = 100) => {
      return description.length > length
        ? description.substring(0, length) + '...'
        : description
    }

    const toggleFullDescription = (record) => {
      record.showFullDescription = !record.showFullDescription
    }

    const handleRecordAdded = () => {
      fetchHealthRecords()
      showAddForm.value = false
    }

    onMounted(fetchHealthRecords)

    return {
      healthRecords,
      loading,
      error,
      showAddForm,
      fetchHealthRecords,
      formatDate,
      formatRecordType,
      truncateDescription,
      toggleFullDescription,
      handleRecordAdded
    }
  }
}
</script>

<style scoped>
.health-record {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.page-title {
  font-size: 2rem;
  color: #2c5282;
  margin-bottom: 1.5rem;
  text-align: center;
}

.loading, .error {
  text-align: center;
  font-size: 1.2rem;
  color: #4a5568;
  margin-top: 2rem;
}

.health-records-list {
  display: grid;
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

.health-record-card {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.record-title {
  font-size: 1.25rem;
  color: #2c5282;
  margin-bottom: 0.5rem;
}

.record-date {
  font-size: 0.9rem;
  color: #718096;
  margin-bottom: 0.5rem;
}

.record-description {
  color: #4a5568;
  margin-bottom: 1rem;
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
  margin-top: 1rem;
}

.btn-primary:hover {
  background-color: #2779bd;
}

.btn-secondary {
  background-color: #6cb2eb;
  color: white;
  border: none;
}

.btn-secondary:hover {
  background-color: #4e9ae1;
}
</style>