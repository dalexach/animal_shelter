<template>
  <div class="add-animal">
    <h2 class="title">Agregar Nuevo Animal</h2>
    <form @submit.prevent="submitForm" class="animal-form">
      <div class="form-group">
        <label for="nombre">Nombre:</label>
        <input v-model="animal.nombre" type="text" id="nombre" required>
      </div>
      <div class="form-group">
        <label for="especie">Especie:</label>
        <input v-model="animal.especie" type="text" id="especie" required>
      </div>
      <div class="form-group">
        <label for="raza">Raza:</label>
        <input v-model="animal.raza" type="text" id="raza">
      </div>
      <div class="form-group">
        <label for="edad">Edad:</label>
        <input v-model="animal.edad" type="number" id="edad" required>
      </div>
      <div class="form-group">
        <label for="peso">Peso (kg):</label>
        <input v-model="animal.peso" type="number" step="0.1" id="peso" required>
      </div>
      <div class="form-group">
        <label for="altura">Altura (cm):</label>
        <input v-model="animal.altura" type="number" step="0.1" id="altura" required>
      </div>
      <div class="form-group">
        <label for="sexo">Sexo:</label>
        <select v-model="animal.sexo" id="sexo" required>
          <option value="M">Macho</option>
          <option value="H">Hembra</option>
        </select>
      </div>
      <button type="submit" class="submit-btn">Agregar Animal</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  name: 'AddAnimal',
  setup() {
    const animal = ref({
      nombre: '',
      especie: '',
      raza: '',
      edad: null,
      peso: null,
      altura: null,
      sexo: ''
    })

    const submitForm = async () => {
      try {
        console.log('Datos del animal a enviar:', animal.value)
        const response = await axios.post('https://animalshelter-27633f1524c4.herokuapp.com/api/animales/', animal.value)
        console.log('Animal agregado exitosamente:', response.data)
        // Limpiar el formulario
        animal.value = {
          nombre: '',
          especie: '',
          raza: '',
          edad: null,
          peso: null,
          altura: null,
          sexo: ''
        }
        alert('Animal agregado exitosamente')
      } catch (error) {
        console.error('Error al agregar el animal:', error)
        if (error.response) {
          console.log('Datos de la respuesta:', error.response.data)
          alert(`Error: ${JSON.stringify(error.response.data)}`)
        } else if (error.request) {
          console.log('Solicitud:', error.request)
          alert('Error de red. Por favor, intenta de nuevo.')
        } else {
          console.log('Mensaje de error:', error.message)
          alert('Error desconocido. Por favor, intenta de nuevo.')
        }
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
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f0f8ff; /* Alice Blue */
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.title {
  color: #2c5282; /* Dark Blue */
  text-align: center;
  margin-bottom: 20px;
}

.animal-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #2b6cb0; /* Medium Blue */
}

input, select {
  width: 100%;
  padding: 8px;
  border: 1px solid #90cdf4; /* Light Blue */
  border-radius: 4px;
  background-color: #ebf8ff; /* Very Light Blue */
}

input:focus, select:focus {
  outline: none;
  border-color: #3182ce; /* Bright Blue */
  box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.5); /* Blue glow */
}

.submit-btn {
  background-color: #3182ce; /* Bright Blue */
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #2c5282; /* Dark Blue */
}

.submit-btn:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.5); /* Blue glow */
}
</style>