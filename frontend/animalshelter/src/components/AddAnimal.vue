<template>
  <div class="add-animal">
    <h2>Añadir Nuevo Animal</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" v-model="animal.nombre" required>
      </div>
      <div>
        <label for="especie">Especie:</label>
        <input type="text" id="especie" v-model="animal.especie" required>
      </div>
      <div>
        <label for="habitat">Hábitat:</label>
        <input type="text" id="habitat" v-model="animal.habitat" required>
      </div>
      <div>
        <label for="tipo_comida">Tipo de Comida:</label>
        <input type="text" id="tipo_comida" v-model="animal.tipo_comida" required>
      </div>
      <div>
        <label for="marca_comida">Marca de Comida:</label>
        <input type="text" id="marca_comida" v-model="animal.marca_comida" required>
      </div>
      <div>
        <label for="necesidades_aseo">Necesidades de Aseo:</label>
        <textarea id="necesidades_aseo" v-model="animal.necesidades_aseo" required></textarea>
      </div>
      <div>
        <label for="necesidades_aseo_habitat">Necesidades de Aseo del Hábitat:</label>
        <textarea id="necesidades_aseo_habitat" v-model="animal.necesidades_aseo_habitat" required></textarea>
      </div>
      <button type="submit">Añadir Animal</button>
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
  max-width: 500px;
  margin: 0 auto;
  padding: 20px;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 10px;
}

input, textarea {
  width: 100%;
  padding: 5px;
  margin-top: 5px;
}

button {
  margin-top: 20px;
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}
</style>