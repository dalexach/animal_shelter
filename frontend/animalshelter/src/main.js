import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

// Configurar Axios para incluir el token en todas las solicitudes
axios.interceptors.request.use(config => {
  const token = store.state.token || localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
}, error => {
  return Promise.reject(error)
})

// Interceptor para manejar errores de respuesta
axios.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 401) {
      // Token expirado o inválido, redirigir al login
      store.commit('setToken', null)
      localStorage.removeItem('token')
      router.push('/login')
    }
    return Promise.reject(error)
  }
)

createApp(App).use(router).use(store).mount('#app')