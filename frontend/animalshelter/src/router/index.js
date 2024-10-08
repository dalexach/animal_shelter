import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Animals from '../views/Animals.vue'
import AnimalDetails from '../components/AnimalDetails.vue'
import AddAnimal from '../components/AddAnimal.vue'
import Caregivers from '../views/Caregivers.vue'
import CaregiverDetails from '../components/CaregiverDetails.vue'
import AddCaregiver from '../components/AddCaregiver.vue'
import Reports from '../views/Reports.vue'
import Login from '../components/Login.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: true }
  },
  {
    path: '/animals',
    name: 'Animals',
    component: Animals,
    meta: { requiresAuth: true }
  },
  {
    path: '/animals/:id',
    name: 'AnimalDetails',
    component: AnimalDetails,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: '/add-animal',
    name: 'AddAnimal',
    component: AddAnimal,
    meta: { requiresAuth: true }
  },
  {
    path: '/caregivers',
    name: 'Caregivers',
    component: Caregivers,
    meta: { requiresAuth: true }
  },
  {
    path: '/caregivers/:id',
    name: 'CaregiverDetails',
    component: CaregiverDetails,
    props: true,
    meta: { requiresAuth: true }
  },
  {
    path: '/add-caregiver',
    name: 'AddCaregiver',
    component: AddCaregiver,
    meta: { requiresAuth: true }
  },
  {
    path: '/reports',
    name: 'Reports',
    component: Reports,
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)
  const loggedIn = localStorage.getItem('token')

  if (requiresAuth && !loggedIn) {
    next('/login')
  } else {
    next()
  }
})

export default router