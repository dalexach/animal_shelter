<template>
  <div class="add-animal">
    <h2 class="page-title">Agregar Nuevo Animal</h2>
    <form @submit.prevent="submitForm" class="animal-form">
      <div class="form-group">
        <label for="nombre">Nombre:</label>
        <input v-model="animal.nombre" type="text" id="nombre" required class="form-input">
      </div>
      <div class="form-group">
        <label for="especie">Especie:</label>
        <input v-model="animal.especie" type="text" id="especie" required class="form-input">
      </div>
      <div class="form-group">
        <label for="raza">Raza:</label>
        <input v-model="animal.raza" type="text" id="raza" class="form-input">
      </div>
      <div class="form-group">
        <label for="edad">Edad:</label>
        <input v-model="animal.edad" type="number" id="edad" required class="form-input">
      </div>
      <div class="form-group">
        <label for="peso">Peso:</label>
        <input v-model="animal.peso" type="number" id="peso" step="0.1" required class="form-input">
      </div>
      <div class="form-group">
        <label for="altura">Altura:</label>
        <input v-model="animal.altura" type="number" id="altura" step="0.1" required class="form-input">
      </div>
      <div class="form-group">
        <label for="sexo">Sexo:</label>
        <select v-model="animal.sexo" id="sexo" required class="form-select">
          <option value="M">Macho</option>
          <option value="H">Hembra</option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary">Agregar Animal</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export default {
  name: 'AddAnimal',
  setup() {
    const router = useRouter()
    const animal = ref({
      nombre: '',
      especie: '',
      habitat: '',
      tipo_comida: '',
      marca_comida: '',
      necesidades_aseo: '',
      necesidades_aseo_habitat: ''
    })

    const submitForm = async () => {
      try {
        await axios.post('https://animalshelter-27633f1524c4.herokuapp.com/api/animales/', animal.value)
        router.push({ name: 'Animals' })
      } catch (error) {
        console.error('Error adding animal:', error)
      }
    }

    return {
      animal,
      submitForm
    }
  }
}
</script>

<style scoped>
.add-animal {
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

.animal-form {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #4a5568;
}

.form-input,
.form-select {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
  font-size: 1rem;
}

.form-select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3E%3Cpath stroke='%236b7280' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3E%3C/svg%3E");
  background-position: right 0.5rem center;
  background-repeat: no-repeat;
  background-size: 1.5em 1.5em;
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
</style>