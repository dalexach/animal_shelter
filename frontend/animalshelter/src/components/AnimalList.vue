<template>
  <div class="animal-list">
    <h2 class="page-title">Lista de Animales</h2>
    <div class="search-bar">
      <input v-model="searchTerm" type="text" placeholder="Buscar animales..." class="search-input">
    </div>
    <div class="animal-grid">
      <div v-for="animal in filteredAnimals" :key="animal.id" class="animal-card">
        <h3 class="animal-name">{{ animal.nombre }}</h3>
        <p><strong>Especie:</strong> {{ animal.especie }}</p>
        <p><strong>Edad:</strong> {{ animal.edad }} años</p>
        <p><strong>Sexo:</strong> {{ animal.sexo === 'M' ? 'Macho' : 'Hembra' }}</p>
        <router-link :to="{ name: 'AnimalDetails', params: { id: animal.id } }" class="btn btn-primary">Ver Detalles</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'AnimalList',
  setup() {
    const animals = ref([]);
    const searchTerm = ref('');

    const fetchAnimals = async () => {
      try {
        const response = await axios.get('https://animalshelter-27633f1524c4.herokuapp.com/animales/');
        animals.value = response.data;
      } catch (error) {
        console.error('Error fetching animals:', error);
      }
    };

    const filteredAnimals = computed(() => {
      return animals.value.filter(animal =>
        animal.nombre.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
        animal.especie.toLowerCase().includes(searchTerm.value.toLowerCase())
      );
    });

    onMounted(fetchAnimals);

    return {
      animals,
      searchTerm,
      filteredAnimals
    };
  }
};
</script>

<style scoped>
.animal-list {
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

.animal-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
}

.animal-card {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.animal-name {
  font-size: 1.25rem;
  color: #2c5282;
  margin-bottom: 0.5rem;
}

.animal-card p {
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