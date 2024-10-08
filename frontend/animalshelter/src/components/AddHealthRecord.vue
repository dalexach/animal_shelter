<template>
  <div class="add-health-record">
    <h3>Añadir Registro de Salud</h3>
    <form @submit.prevent="submitForm">
      <div>
        <label for="tipo">Tipo:</label>
        <select id="tipo" v-model="record.tipo" required>
          <option value="examen">Examen de Laboratorio</option>
          <option value="vacuna">Vacuna</option>
          <option value="control">Control Médico</option>
          <option value="enfermedad">Enfermedad</option>
        </select>
      </div>
      <div>
        <label for="descripcion">Descripción:</label>
        <textarea id="descripcion" v-model="record.descripcion" required></textarea>
      </div>
      <div>
        <label for="fecha">Fecha:</label>
        <input type="date" id="fecha" v-model="record.fecha" required>
      </div>
      <button type="submit">Guardar</button>
      <button type="button" @click="$emit('cancel')">Cancelar</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  name: 'AddHealthRecord',
  props: {
    animalId: {
      type: Number,
      required: true
    }
  },
  emits: ['recordAdded', 'cancel'],
  setup(props, { emit }) {
    const record = ref({
      tipo: '',
      descripcion: '',
      fecha: '',
      animal: props.animalId
    })

    const submitForm = async () => {
      try {
        await axios.post('https://animalshelter-27633f1524c4.herokuapp.com/api/registros-salud/', record.value)
        emit('recordAdded')
        emit('cancel')
      } catch (error) {
        console.error('Error adding health record:', error)
      }
    }

    return {
      record,
      submitForm
    }
  }
}
</script>

<style scoped>
.add-health-record {
  margin-top: 20px;
  border: 1px solid #ddd;
  padding: 20px;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 10px;
}

input, select, textarea {
  width: 100%;
  padding: 5px;
  margin-top: 5px;
}

button {
  margin-top: 10px;
  padding: 5px 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

button[type="button"] {
  background-color: #f44336;
}
</style>