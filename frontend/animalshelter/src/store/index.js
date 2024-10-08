import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    token: localStorage.getItem('token') || null
  },
  mutations: {
    setUser(state, user) {
      state.user = user
    },
    setToken(state, token) {
      state.token = token
      if (token) {
        localStorage.setItem('token', token)
      } else {
        localStorage.removeItem('token')
      }
    },
    logout(state) {
      state.user = null
      state.token = null
      localStorage.removeItem('token')
    }
  },
  actions: {
    login({ commit }, { token, user }) {
      commit('setToken', token)
      commit('setUser', user)
    },
    logout({ commit }) {
      commit('logout')
    },
    checkAuth({ commit, state }) {
      if (state.token) {
        // Aquí podrías hacer una llamada a la API para verificar si el token es válido
        // y obtener la información del usuario si es necesario
        // Por ahora, solo asumiremos que el token es válido si existe
        commit('setUser', { id: 'placeholder', username: 'Usuario' })
      } else {
        commit('logout')
      }
    }
  },
  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.user
  }
})