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
      localStorage.setItem('token', token)
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
    }
  },
  getters: {
    isLoggedIn: state => !!state.token
  }
})