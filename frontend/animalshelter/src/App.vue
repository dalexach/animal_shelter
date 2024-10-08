<template>
  <div id="app">
    <header>
      <h1>Refugio de Animales</h1>
      <nav v-if="isLoggedIn">
        <router-link to="/">Inicio</router-link> |
        <router-link to="/animals">Animales</router-link> |
        <router-link to="/caregivers">Cuidadores</router-link> |
        <router-link to="/reports">Reportes</router-link> |
        <a href="#" @click.prevent="logout">Cerrar Sesión</a>
      </nav>
    </header>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

export default {
  name: 'App',
  setup() {
    const store = useStore()
    const router = useRouter()

    const isLoggedIn = computed(() => store.getters.isLoggedIn)

    const logout = () => {
      store.dispatch('logout')
      router.push('/login')
    }

    return {
      isLoggedIn,
      logout
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

header {
  background-color: #4CAF50;
  color: white;
  padding: 10px;
  text-align: center;
}

nav {
  margin-top: 10px;
}

nav a {
  color: white;
  text-decoration: none;
  margin: 0 10px;
}

main {
  padding: 20px;
}
</style>