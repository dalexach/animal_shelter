<template>
  <div class="animals-view">
    <h1 class="page-title">Listado de Animales</h1>
    <router-link to="/add-animal" class="btn btn-primary mb-4">Agregar Animal</router-link>
    <AnimalList />
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import AnimalList from '@/components/AnimalList.vue'

export default defineComponent({
  name: 'Animals',
  components: {
    AnimalList
  }
})
</script>

<style scoped>
.animals-view {
  padding: 20px;
}

.page-title {
  font-size: 2rem;
  color: #2c5282;
  margin-bottom: 1.5rem;
  text-align: center;
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
}

.btn-primary {
  background-color: #3490dc;
  color: white;
}

.btn-primary:hover {
  background-color: #2779bd;
}

.mb-4 {
  margin-bottom: 1rem;
}
</style>