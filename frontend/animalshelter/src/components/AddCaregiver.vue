<template>
  <div class="add-caregiver">
    <h2>Añadir Nuevo Cuidador</h2>
    <form @submit.prevent="submitForm">
      <div>
        <label for="username">Nombre de Usuario:</label>
        <input type="text" id="username" v-model="caregiver.username" required>
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="caregiver.email" required>
      </div>
      <div>
        <label for="password">Contraseña:</label>
        <input type="password" id="password" v-model="caregiver.password" required>
      </div>
      <div>
        <label for="nombre_completo">Nombre Completo:</label>
        <input type="text" id="nombre_completo" v-model="caregiver.nombre_completo" required>
      </div>
      <div>
        <label for="numero_celular">Número de Celular:</label>
        <input type="tel" id="numero_celular" v-model="caregiver.numero_celular" required>
      </div>
      <button type="submit">Añadir Cuidador</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

export default {
  name: 'AddCaregiver',
  setup() {
    const router = useRouter()
    const caregiver = ref({
      username: '',
      email: '',
      password: '',
      nombre_completo: '',
      numero_celular: ''
    })

    const submitForm = async () => {
      try {
        await axios.post('https://animalshelter-27633f1524c4.herokuapp.com/api/cuidadores/', caregiver.value)
        router.push({ name: 'Caregivers' })
      } catch (error) {
        console.error('Error adding caregiver:', error)
      }
    }

    return {
      caregiver,
      submitForm
    }
  }
}
</script>



<style scoped>
.add-caregiver {
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

input {
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