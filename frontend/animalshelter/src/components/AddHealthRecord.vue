<template>
  <div class="add-health-record">
    <h2 class="page-title">Agregar Registro de Salud</h2>
    <form @submit.prevent="submitForm" class="health-record-form">
      <div class="form-group">
        <label for="animal">Animal:</label>
        <select v-model="healthRecord.animal" id="animal" required class="form-select">
          <option v-for="animal in animals" :key="animal.id" :value="animal.id">
            {{ animal.nombre }} ({{ animal.especie }})
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="fecha">Fecha:</label>
        <input v-model="healthRecord.fecha" type="date" id="fecha" required class="form-input">
      </div>
      <div class="form-group">
        <label for="tipo_registro">Tipo de Registro:</label>
        <select v-model="healthRecord.tipo_registro" id="tipo_registro" required class="form-select">
          <option value="vacuna">Vacuna</option>
          <option value="examen">Examen</option>
          <option value="tratamiento">Tratamiento</option>
        </select>
      </div>
      <div class="form-group">
        <label for="descripcion">Descripción:</label>
        <textarea v-model="healthRecord.descripcion" id="descripcion" required class="form-textarea"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Agregar Registro</button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  name: 'AddHealthRecord',
  setup() {
    const animals = ref([]);
    const healthRecord = ref({
      animal: '',
      fecha: '',
      tipo_registro: '',
      descripcion: ''
    });

    const fetchAnimals = async () => {
      try {
        const response = await axios.get('https://animalshelter-27633f1524c4.herokuapp.com/animales/');
        animals.value = response.data;
      } catch (error) {
        console.error('Error fetching animals:', error);
      }
    };

    const submitForm = async () => {
      try {
        await axios.post('https://animalshelter-27633f1524c4.herokuapp.com/registros-salud/', healthRecord.value);
        alert('Registro de salud agregado exitosamente');
        // Limpiar el formulario o redirigir según sea necesario
      } catch (error) {
        console.error('Error adding health record:', error);
        alert('Error al agregar el registro de salud');
      }
    };

    onMounted(fetchAnimals);

    return {
      animals,
      healthRecord,
      submitForm
    };
  }
};
</script>

<style scoped>
.add-health-record {
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

.health-record-form {
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
.form-select,
.form-textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
  font-size: 1rem;
}

.form-textarea {
  min-height: 100px;
  resize: vertical;
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