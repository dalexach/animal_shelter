<template>
  <div class="add-caregiver">
    <h2 class="page-title">Agregar Nuevo Cuidador</h2>
    <form @submit.prevent="submitForm" class="caregiver-form">
      <div class="form-group">
        <label for="nombre">Nombre:</label>
        <input v-model="caregiver.nombre" type="text" id="nombre" required class="form-input">
      </div>
      <div class="form-group">
        <label for="apellido">Apellido:</label>
        <input v-model="caregiver.apellido" type="text" id="apellido" required class="form-input">
      </div>
      <div class="form-group">
        <label for="identificacion">Identificación:</label>
        <input v-model="caregiver.identificacion" type="text" id="identificacion" required class="form-input">
      </div>
      <div class="form-group">
        <label for="telefono">Teléfono:</label>
        <input v-model="caregiver.telefono" type="tel" id="telefono" required class="form-input">
      </div>
      <div class="form-group">
        <label for="direccion">Dirección:</label>
        <input v-model="caregiver.direccion" type="text" id="direccion" required class="form-input">
      </div>
      <div class="form-group">
        <label for="fecha_nacimiento">Fecha de Nacimiento:</label>
        <input v-model="caregiver.fecha_nacimiento" type="date" id="fecha_nacimiento" required class="form-input">
      </div>
      <button type="submit" class="btn btn-primary">Agregar Cuidador</button>
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

.caregiver-form {
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

.form-input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
  font-size: 1rem;
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