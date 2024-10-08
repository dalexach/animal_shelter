<template>
  <div class="animals">
    <h1>Gestión de Animales</h1>
    <router-link to="/add-animal" class="btn-add">Añadir Nuevo Animal</router-link>
    <AnimalList />
  </div>
</template>

<script>
import AnimalList from '@/components/AnimalList.vue'

export default {
  name: 'Animals',
  components: {
    AnimalList
  }
}
</script>

<style scoped>
.animals {
  max-width: 1200px;
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