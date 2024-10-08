<template>
  <div class="caregiver-details" v-if="caregiver">
    <h2>{{ caregiver.nombre_completo }}</h2>
    <p><strong>Email:</strong> {{ caregiver.email }}</p>
    <p><strong>Número de Celular:</strong> {{ caregiver.numero_celular }}</p>
    <h3>Animales a Cargo</h3>
    <ul v-if="caregiver.animales && caregiver.animales.length">
      <li v-for="animal in caregiver.animales" :key="animal.id">
        <router-link :to="{ name: 'AnimalDetails', params: { id: animal.id } }">
          {{ animal.nombre }}
        </router-link>
      </li>
    </ul>
    <p v-else>Este cuidador no tiene animales asignados actualmente.</p>
  </div>
  <div v-else>Cargando detalles del cuidador...</div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'CaregiverDetails',
  props: {
    id: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const caregiver = ref(null)

    const fetchCaregiverDetails = async () => {
      try {
        const response = await axios.get(`https://animalshelter-27633f1524c4.herokuapp.com/api/cuidadores/${props.id}/`)
        caregiver.value = response.data
      } catch (error) {
        console.error('Error fetching caregiver details:', error)
      }
    }

    onMounted(fetchCaregiverDetails)

    return {
      caregiver
    }
  }
}
</script>

<style scoped>
.caregiver-details {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

h3 {
  margin-top: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

a {
  color: #4CAF50;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
</style>