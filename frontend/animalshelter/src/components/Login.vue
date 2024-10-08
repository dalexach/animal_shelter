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
      <button type="submit" class="login-button">Iniciar Sesión</button>
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

<style scoped>
.login-container {
  max-width: 400px;
  margin: 2rem auto;
  padding: 2rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

h2 {
  text-align: center;
  color: #333;
  margin-bottom: 1.5rem;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #555;
}

input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.login-button {
  background-color: #4CAF50;
  color: white;
  padding: 0.75rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s;
}

.login-button:hover {
  background-color: #45a049;
}

.error-message {
  color: #ff0000;
  text-align: center;
  margin-top: 1rem;
}
</style>