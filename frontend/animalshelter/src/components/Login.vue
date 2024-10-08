<template>
  <div class="login-container">
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="handleSubmit" class="login-form">
      <div class="form-group">
        <label for="username">Nombre de Usuario:</label>
        <input
          id="username"
          v-model="username"
          type="text"
          required
          placeholder="Ingrese su nombre de usuario"
        >
      </div>
      <div class="form-group">
        <label for="password">Contraseña:</label>
        <input
          id="password"
          v-model="password"
          type="password"
          required
          placeholder="Ingrese su contraseña"
        >
      </div>
      <button type="submit" class="login-button" :disabled="isLoading">
        {{ isLoading ? 'Iniciando sesión...' : 'Iniciar Sesión' }}
      </button>
      <p v-if="error" class="error-message">{{ error }}</p>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      username: '',
      password: '',
      error: '',
      isLoading: false
    }
  },
  methods: {
    async handleSubmit() {
      this.isLoading = true
      this.error = ''
      try {
        const response = await axios.post('https://animalshelter-27633f1524c4.herokuapp.com/api/token/', {
          username: this.username,
          password: this.password
        })
        localStorage.setItem('token', response.data.access)
        this.$router.push('/')
      } catch (error) {
        console.error('Error completo:', error)
        if (error.response) {
          console.error('Datos de respuesta:', error.response.data)
          console.error('Estado de respuesta:', error.response.status)
          console.error('Cabeceras de respuesta:', error.response.headers)
          this.error = error.response.data.detail || 'Error al iniciar sesión'
        } else if (error.request) {
          console.error('Solicitud:', error.request)
          this.error = 'No se recibió respuesta del servidor'
        } else {
          console.error('Error de configuración:', error.message)
          this.error = 'Error al configurar la solicitud'
        }
      } finally {
        this.isLoading = false
      }
    }
  }
}
</script>

<style scoped>
/* ... (mantén los estilos existentes) ... */
.login-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
</style>