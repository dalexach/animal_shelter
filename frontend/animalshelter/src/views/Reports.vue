<template>
  <div class="reports-view">
    <h1 class="page-title">Reportes</h1>
    <div class="report-options">
      <button @click="generateReport('animals')" class="btn btn-primary">Reporte de Animales</button>
      <button @click="generateReport('caregivers')" class="btn btn-primary">Reporte de Cuidadores</button>
      <button @click="generateReport('adoptions')" class="btn btn-primary">Reporte de Adopciones</button>
    </div>
    <div v-if="reportData" class="report-container">
      <h2 class="report-title">{{ reportTitle }}</h2>
      <table class="report-table">
        <thead>
          <tr>
            <th v-for="header in reportHeaders" :key="header">{{ header }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="row in reportData" :key="row.id">
            <td v-for="header in reportHeaders" :key="header">{{ row[header] }}</td>
          </tr>
        </tbody>
      </table>
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
  .reports-view {
    padding: 20px;
  }

  .page-title {
    font-size: 2rem;
    color: #2c5282;
    margin-bottom: 1.5rem;
    text-align: center;
  }

  .report-options {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 2rem;
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

  .report-container {
    background-color: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }

  .report-title {
    font-size: 1.5rem;
    color: #2c5282;
    margin-bottom: 1rem;
    text-align: center;
  }

  .report-table {
    width: 100%;
    border-collapse: collapse;
  }

  .report-table th,
  .report-table td {
    padding: 0.75rem;
    text-align: left;
    border-bottom: 1px solid #e2e8f0;
  }

  .report-table th {
    background-color: #edf2f7;
    font-weight: bold;
    color: #2c5282;
  }

  .report-table tr:nth-child(even) {
    background-color: #f7fafc;
  }

  .report-table tr:hover {
    background-color: #e6f3ff;
  }
</style>