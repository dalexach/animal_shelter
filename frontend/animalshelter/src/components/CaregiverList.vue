<template>
  <div class="caregiver-list">
    <h2 class="page-title">Lista de Cuidadores</h2>
    <div class="search-bar">
      <input v-model="searchTerm" type="text" placeholder="Buscar cuidadores..." class="search-input">
    </div>
    <div class="caregiver-grid">
      <div v-for="caregiver in filteredCaregivers" :key="caregiver.id" class="caregiver-card">
        <h3 class="caregiver-name">{{ caregiver.nombre }} {{ caregiver.apellido }}</h3>
        <p><strong>Identificación:</strong> {{ caregiver.identificacion }}</p>
        <p><strong>Teléfono:</strong> {{ caregiver.telefono }}</p>
        <router-link :to="{ name: 'CaregiverDetails', params: { id: caregiver.id } }" class="btn btn-primary">Ver Detalles</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'CaregiverList',
  setup() {
    const caregivers = ref([]);
    const searchTerm = ref('');

    const fetchCaregivers = async () => {
      try {
        const response = await axios.get('https://animalshelter-27633f1524c4.herokuapp.com/cuidadores/');
        caregivers.value = response.data;
      } catch (error) {
        console.error('Error fetching caregivers:', error);
      }
    };

    const filteredCaregivers = computed(() => {
      return caregivers.value.filter(caregiver =>
        caregiver.nombre.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
        caregiver.apellido.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
        caregiver.identificacion.includes(searchTerm.value)
      );
    });

    onMounted(fetchCaregivers);

    return {
      caregivers,
      searchTerm,
      filteredCaregivers
    };
  }
};
</script>

<style scoped>
.caregiver-list {
  padding: 20px;
}

.page-title {
  font-size: 2rem;
  color: #2c5282;
  margin-bottom: 1.5rem;
  text-align: center;
}

.search-bar {
  margin-bottom: 1.5rem;
}

.search-input {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
}

.caregiver-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

.caregiver-card {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.caregiver-name {
  font-size: 1.25rem;
  color: #2c5282;
  margin-bottom: 0.5rem;
}

.caregiver-card p {
  margin-bottom: 0.5rem;
  color: #4a5568;
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
</style>