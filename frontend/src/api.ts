import axios from 'axios'
import type { Task } from '@/models/Task'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/'
})

export const fetchTasks = async (): Promise<Task[]> => {
  try {
    const response = await api.get<Task[]>('tasks/')
    return response.data
  } catch (error) {
    console.error('Error fetching tasks:', error)
  }
}

export const addTask = async (task: Task): Promise<void> => {
  try {
    const response = await api.post('tasks/', task)
    return response.data
  } catch (error) {
    console.error('Error adding task:', error)
  }
}

export const updateTask = async (task: Task): Promise<void> => {
  try {
    await api.put(`tasks/${task.id}/`, task)
    console.log('Task updated successfully', task)
  } catch (error) {
    console.error('Error updating task:', error)
  }
}

export const completeTask = async (task: Task): Promise<void> => {
  try {
    await api.post(`tasks/${task.id}/complete/`)
    console.log('Task completing successfully', task)
  } catch (error) {
    console.error('Error completing task:', error)
  }
}
