<template>
  <div class="dashboard">
    <h1 class="page-title">Panel de Control</h1>
    <div class="dashboard-grid">
      <div class="dashboard-card">
        <h2 class="card-title">Resumen de Animales</h2>
        <p class="card-stat">Total de animales: {{ animalStats.total }}</p>
        <p class="card-stat">Perros: {{ animalStats.dogs }}</p>
        <p class="card-stat">Gatos: {{ animalStats.cats }}</p>
        <p class="card-stat">Otros: {{ animalStats.others }}</p>
      </div>
      <div class="dashboard-card">
        <h2 class="card-title">Resumen de Cuidadores</h2>
        <p class="card-stat">Total de cuidadores: {{ caregiverStats.total }}</p>
        <p class="card-stat">Cuidadores activos: {{ caregiverStats.active }}</p>
      </div>
      <div class="dashboard-card">
        <h2 class="card-title">Registros de Salud</h2>
        <p class="card-stat">Total de registros: {{ healthRecordStats.total }}</p>
        <p class="card-stat">Registros este mes: {{ healthRecordStats.thisMonth }}</p>
      </div>
      <div class="dashboard-card">
        <h2 class="card-title">Acciones Rápidas</h2>
        <div class="quick-actions">
          <router-link to="/add-animal" class="btn btn-primary">Agregar Animal</router-link>
          <router-link to="/add-caregiver" class="btn btn-secondary">Agregar Cuidador</router-link>
          <router-link to="/add-health-record" class="btn btn-tertiary">Nuevo Registro de Salud</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'Dashboard',
  setup() {
    const animalStats = ref({ total: 0, dogs: 0, cats: 0, others: 0 });
    const caregiverStats = ref({ total: 0, active: 0 });
    const healthRecordStats = ref({ total: 0, thisMonth: 0 });

    const fetchDashboardData = async () => {
      try {
        const response = await axios.get('https://animalshelter-27633f1524c4.herokuapp.com/dashboard/');
        animalStats.value = response.data.animal_stats;
        caregiverStats.value = response.data.caregiver_stats;

        healthRecordStats.value = response.data.health_record_stats;
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      }
    };

    onMounted(fetchDashboardData);

    return {
      animalStats,
      caregiverStats,
      healthRecordStats
    };
  }
};
</script>

<style scoped>
.dashboard {
  padding: 20px;
}

.page-title {
  font-size: 2.5rem;
  color: #2c5282;
  margin-bottom: 2rem;
  text-align: center;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.dashboard-card {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.card-title {
  font-size: 1.5rem;
  color: #2c5282;
  margin-bottom: 1rem;
}

.card-stat {
  font-size: 1.1rem;
  color: #4a5568;
  margin-bottom: 0.5rem;
}

.quick-actions {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.btn {
  display: inline-block;
  padding: 0.75rem 1rem;
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

.btn-tertiary {
  background-color: #9ae6b4;
  color: #22543d;
}

.btn-tertiary:hover {
  background-color: #68d391;
}
</style>