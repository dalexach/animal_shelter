<template>
  <div class="caregivers-view">
    <h1 class="page-title">Listado de Cuidadores</h1>
    <router-link to="/add-caregiver" class="btn btn-primary mb-4">Agregar Cuidador</router-link>
    <div class="caregiver-grid">
      <div v-for="caregiver in caregivers" :key="caregiver.id" class="caregiver-card">
        <h2 class="caregiver-name">{{ caregiver.nombre }} {{ caregiver.apellido }}</h2>
        <p><strong>Identificación:</strong> {{ caregiver.identificacion }}</p>
        <p><strong>Teléfono:</strong> {{ caregiver.telefono }}</p>
        <router-link :to="{ name: 'CaregiverDetails', params: { id: caregiver.id } }" class="btn btn-secondary">Ver Detalles</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import CaregiverList from '@/components/CaregiverList.vue'

export default {
  name: 'Caregivers',
  components: {
    CaregiverList
  }
}
</script>


<style scoped>
.caregivers-view {
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
</style>