<template>
  <div class="reports">
    <h1>Reportes</h1>
    <div class="report-options">
      <button @click="generateReport('animal')">Generar Reporte por Animal</button>
      <button @click="generateReport('caregiver')">Generar Reporte por Cuidador</button>
    </div>
    <div v-if="loading">Generando reporte...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else-if="report">
      <h2>{{ reportTitle }}</h2>
      <pre>{{ JSON.stringify(report, null, 2) }}</pre>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  name: 'Reports',
  setup() {
    const report = ref(null)
    const loading = ref(false)
    const error = ref(null)
    const reportTitle = ref('')

    const generateReport = async (type) => {
      loading.value = true
      error.value = null
      report.value = null

      try {
        const response = await axios.post('https://animalshelter-27633f1524c4.herokuapp.com/api/reportes/', { tipo: type })
        report.value = response.data
        reportTitle.value = type === 'animal' ? 'Reporte por Animal' : 'Reporte por Cuidador'
      } catch (e) {
        error.value = 'Error al generar el reporte'
      } finally {
        loading.value = false
      }
    }

    return {
      report,
      loading,
      error,
      reportTitle,
      generateReport
    }
  }
}
</script>

<style scoped>
.reports {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.report-options {
  margin-bottom: 20px;
}

button {
  margin-right: 10px;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

pre {
  background-color: #f4f4f4;
  padding: 15px;
  border-radius: 5px;
  white-space: pre-wrap;
  word-wrap: break-word;
}
</style>