<template>
  <div class="tasks">
    <h1>Tasks</h1>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <h2>{{ task.title }}</h2>
        <p>Description: {{ task.description }}</p>
        <p>Type: {{ task.task_type }}</p>
        <p>Status: {{ task.completed ? 'Completed' : 'Pending' }}</p>
        <p>Due Date: {{ new Date(task.due_date).toLocaleDateString() }}</p>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import axios from 'axios'
import type { Task } from '@/models/Task'

export default defineComponent({
  setup() {
    const tasks = ref<Task[]>([])

    const fetchTasks = async () => {
      try {
        const response = await axios.get<Task[]>('http://127.0.0.1:8000/api/tasks/')
        tasks.value = response.data
      } catch (error) {
        console.error('Error fetching tasks:', error)
      }
    }

    onMounted(() => {
      fetchTasks()
    })

    return {
      tasks
    }
  }
})
</script>

<style scoped>
h1 {
  font-size: 24px;
}
h2 {
  font-size: 20px;
}
</style>
<script setup lang="ts"></script>
