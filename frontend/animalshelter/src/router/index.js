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
    component: Home
  },
  {
    path: '/animals',
    name: 'Animals',
    component: Animals
  },
  {
    path: '/animals/:id',
    name: 'AnimalDetails',
    component: AnimalDetails,
    props: true
  },
  {
    path: '/add-animal',
    name: 'AddAnimal',
    component: AddAnimal
  },
  {
    path: '/caregivers',
    name: 'Caregivers',
    component: Caregivers
  },
  {
    path: '/caregivers/:id',
    name: 'CaregiverDetails',
    component: CaregiverDetails,
    props: true
  },
  {
    path: '/add-caregiver',
    name: 'AddCaregiver',
    component: AddCaregiver
  },
  {
    path: '/reports',
    name: 'Reports',
    component: Reports
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
  const publicPages = ['/login']
  const authRequired = !publicPages.includes(to.path)
  const loggedIn = localStorage.getItem('token')

  if (authRequired && !loggedIn) {
    return next('/login')
  }

  next()
})

export default router