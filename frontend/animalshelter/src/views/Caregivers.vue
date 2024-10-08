<template>
  <div class="caregivers">
    <h1>Gestión de Cuidadores</h1>
    <router-link to="/add-caregiver" class="btn-add">Añadir Nuevo Cuidador</router-link>
    <CaregiverList />
  </div>
</template>

<script>
import CaregiverList from '@/components/CaregiverList.vue'

export default {
  name: 'Caregivers',
  components: {
    CaregiverList
  }
}
</script>

<style scoped>
.caregivers {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.btn-add {
  display: inline-block;
  margin-bottom: 20px;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}
</style>