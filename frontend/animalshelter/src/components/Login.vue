<template>
  <div class="login-container">
    <div class="login-card">
      <h2 class="login-title">Iniciar Sesión</h2>
      <form @submit.prevent="handleSubmit" class="login-form">
        <div class="form-group">
          <label for="username">Usuario:</label>
          <input v-model="username" type="text" id="username" required class="form-input">
        </div>
        <div class="form-group">
          <label for="password">Contraseña:</label>
          <input v-model="password" type="password" id="password" required class="form-input">
        </div>
        <button type="submit" class="btn btn-primary">Iniciar Sesión</button>
      </form>
      <p v-if="error" class="error-message">{{ error }}</p>
    </div>
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
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f7fafc;
}

.login-card {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

.login-title {
  font-size: 2rem;
  color: #2c5282;
  margin-bottom: 1.5rem;
  text-align: center;
}

.login-form {
  display: flex;
  flex-direction: column;
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
  font-size: 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 4px;
}

.btn {
  display: inline-block;
  padding: 0.75rem 1rem;
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

.error-message {
  color: #e53e3e;
  margin-top: 1rem;
  text-align: center;
}
</style>