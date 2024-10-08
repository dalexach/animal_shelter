<template>
  <div v-if="caregiver" class="caregiver-details">
    <h2>Detalles del Cuidador</h2>
    <p><strong>Nombre:</strong> {{ caregiver.nombre }}</p>
    <p><strong>Apellido:</strong> {{ caregiver.apellido }}</p>
    <p><strong>Identificación:</strong> {{ caregiver.identificacion }}</p>
    <p><strong>Teléfono:</strong> {{ caregiver.telefono }}</p>
    <p><strong>Dirección:</strong> {{ caregiver.direccion }}</p>
    <p><strong>Fecha de Nacimiento:</strong> {{ formatDate(caregiver.fecha_nacimiento) }}</p>
    <button @click="editCaregiver">Editar</button>
    <button @click="deleteCaregiver">Eliminar</button>
  </div>
  <div v-else>
    <p>Cargando detalles del cuidador...</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'

export default {
  name: 'CaregiverDetails',
  setup() {
    const route = useRoute()
    const router = useRouter()
    const caregiver = ref(null)

    const fetchCaregiver = async () => {
      try {
        const response = await axios.get(`https://animalshelter-27633f1524c4.herokuapp.com/api/cuidadores/${route.params.id}/`)
        caregiver.value = response.data
      } catch (error) {
        console.error('Error fetching caregiver details:', error)
      }
    }

    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString()
    }

    const editCaregiver = () => {
      // Implementar lógica de edición
      console.log('Editar cuidador')
    }

    const deleteCaregiver = async () => {
      if (confirm('¿Estás seguro de que quieres eliminar este cuidador?')) {
        try {
          await axios.delete(`https://animalshelter-27633f1524c4.herokuapp.com/api/cuidadores/${route.params.id}/`)
          router.push('/caregivers')
        } catch (error) {
          console.error('Error deleting caregiver:', error)
        }
      }
    }

    onMounted(fetchCaregiver)

    return {
      caregiver,
      formatDate,
      editCaregiver,
      deleteCaregiver
    }
  }
}
</script>

<style scoped>
.caregiver-details {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #2c5282;
  margin-bottom: 20px;
}

p {
  margin-bottom: 10px;
}

button {
  margin-right: 10px;
  padding: 8px 16px;
  background-color: #3490dc;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #2779bd;
}

button:last-child {
  background-color: #e53e3e;
}

button:last-child:hover {
  background-color: #c53030;
}
</style>