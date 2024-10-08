<template>
  <div class="caregiver-list">
    <h2>Lista de Cuidadores</h2>
    <div v-if="loading">Cargando...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
      <ul>
        <li v-for="caregiver in caregivers" :key="caregiver.id">
          <router-link :to="{ name: 'CaregiverDetails', params: { id: caregiver.id } }">
            {{ caregiver.nombre_completo }}
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'CaregiverList',
  setup() {
    const caregivers = ref([])
    const loading = ref(true)
    const error = ref(null)

    const fetchCaregivers = async () => {
      try {
        const response = await axios.get('https://animalshelter-27633f1524c4.herokuapp.com/api/cuidadores/')
        caregivers.value = response.data
        loading.value = false
      } catch (e) {
        error.value = 'Error al cargar los cuidadores'
        loading.value = false
      }
    }

    onMounted(fetchCaregivers)

    return {
      caregivers,
      loading,
      error
    }
  }
}
</script>

<style scoped>
.caregiver-list {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

a {
  color: #4CAF50;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>