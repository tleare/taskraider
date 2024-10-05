<template>
  <div>
    <h1>Tasks</h1>

    <div v-if="tasks.length === 0">No tasks available</div>

    <!-- First row to add a new task -->
    <div class="task-item new-task-row">
      <div class="add-task" @click="toggleNewTask">
        <span class="plus-icon">+</span>
        <input v-model="newTask.title" placeholder="New Task Title" class="editable-field" />
      </div>
      <div v-if="isNewTaskExpanded" class="task-details">
        <label>Description:</label>
        <textarea
          v-model="newTask.description"
          class="editable-field"
          placeholder="Description"
        ></textarea>
        <label>Due Date:</label>
        <input type="date" v-model="newTask.due_date" class="editable-field" />
        <button @click="addTask">Add Task</button>
      </div>
    </div>

    <!-- List of tasks -->
    <ul>
      <li v-for="task in tasks" :key="task.id" class="task-item">
        <div class="task-row" @click="toggleExistingTask(task.id)">
          <input
            type="checkbox"
            :checked="task.completed"
            @change="toggleComplete(task.id)"
            class="task-checkbox"
          />
          <span class="task-title">{{ task.title }}</span>
        </div>
        <div v-if="isExistingTaskExpanded(task.id)" class="task-details">
          <div>
            <label>Title:</label>
            <input v-model="task.title" @blur="saveTask(task.id)" class="editable-field" />
          </div>
          <div>
            <label>Description:</label>
            <textarea
              v-model="task.description"
              @blur="saveTask(task.id)"
              class="editable-field"
            ></textarea>
          </div>
          <div>
            <label>Due Date:</label>
            <input
              type="date"
              v-model="task.due_date"
              @blur="saveTask(task.id)"
              class="editable-field"
            />
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import api from '@/api.ts'
import {completeTask } from '@/api'
import type { Task } from '@/models/Task'

export default defineComponent({
  setup() {
    const tasks = ref<Task[]>([])
    const expandedTaskIds = ref<Set<string>>(new Set())
    const newTask = ref({
      title: '',
      description: '',
      due_date: new Date().toISOString().split('T')[0]
    })
    const isNewTaskExpanded = ref(false)

    const fetchTasks = async () => {
      try {
        const response = await api.get<Task[]>('tasks/')
        tasks.value = response.data
      } catch (error) {
        console.error('Error fetching tasks:', error)
      }
    }

    const toggleExistingTask = (taskId: string) => {
      if (expandedTaskIds.value.has(taskId)) {
        expandedTaskIds.value.delete(taskId)
      } else {
        expandedTaskIds.value.add(taskId)
      }
    }

    const toggleNewTask = () => {
      isNewTaskExpanded.value = !isNewTaskExpanded.value
    }

    const isExistingTaskExpanded = (taskId: string) => {
      return expandedTaskIds.value.has(taskId)
    }

    const saveTask = async (taskId: string) => {
      const task = tasks.value.find((t) => t.id === taskId)
      if (task) {
        try {
          await api.put(`${taskId}/`, task)
          console.log('Task updated successfully')
        } catch (error) {
          console.error('Error updating task:', error)
        }
      }
    }

    const addTask = async () => {
      if (!newTask.value.title) return // Prevent adding empty tasks
      try {
        const response = await api.post('tasks/', newTask.value)
        tasks.value.push(response.data) // Add the newly created task to the list
        // Reset new task input fields
        newTask.value = {
          title: '',
          description: '',
          due_date: new Date().toISOString().split('T')[0]
        }
        isNewTaskExpanded.value = false // Collapse the new task input
      } catch (error) {
        console.error('Error adding task:', error)
      }
    }

    const toggleComplete = async (taskId: string) => {
      const task = tasks.value.find((t) => t.id === taskId)
      if (task) {
        await completeTask(task)
      }
    }

    onMounted(() => {
      fetchTasks()
    })

    return {
      addTask,
      newTask,
      isExistingTaskExpanded,
      isNewTaskExpanded,
      saveTask,
      tasks,
      toggleComplete,
      toggleExistingTask,
      toggleNewTask
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
