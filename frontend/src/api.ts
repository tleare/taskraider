import axios from 'axios'
import type { Task } from '@/models/Task'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/'
})

export default api

export const completeTask = async (task: Task): Promise<void> => {
  try {
    await api.post(`tasks/${task.id}/complete/`)
    console.log('Task completing successfully', task)
  } catch (error) {
    console.error('Error completing task:', error)
  }
}
