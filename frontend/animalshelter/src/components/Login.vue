<template>
  <form @submit.prevent="handleSubmit">
    <input v-model="username" type="text" required>
    <input v-model="password" type="password" required>
    <button type="submit">Login</button>
    <p v-if="error" class="error">{{ error }}</p>
  </form>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      username: '',
      password: '',
      error: ''
    }
  },
  methods: {
    async handleSubmit() {
      try {
        const response = await axios.post('https://animalshelter-27633f1524c4.herokuapp.com/api/token/', {
          username: this.username,
          password: this.password
        })
        localStorage.setItem('token', response.data.access)
        this.$router.push('/')
      } catch (error) {
        if (error.response && error.response.data) {
          this.error = error.response.data.detail || 'Error al iniciar sesión'
        } else {
          this.error = 'Error de conexión'
        }
      }
    }
  }
}
</script>