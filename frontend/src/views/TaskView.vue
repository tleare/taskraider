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
        <input type="datetime-local" v-model="newTask.due_date" class="editable-field" />
        <button @click="addNewTask">Add Task</button>
      </div>
    </div>

    <!-- List of tasks -->
    <ul>
      <li v-for="task in tasks" :key="task.id" class="task-item" :class="{ completed: task.completed }">
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
              type="datetime-local"
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
import { addTask, completeTask, fetchTasks, updateTask } from '@/api'
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

    const loadTasks = async () => {
      tasks.value = await fetchTasks()
    }

    const toggleNewTask = () => {
      isNewTaskExpanded.value = !isNewTaskExpanded.value
    }

    const toggleExistingTask = (taskId: string) => {
      if (expandedTaskIds.value.has(taskId)) {
        expandedTaskIds.value.delete(taskId)
      } else {
        expandedTaskIds.value.add(taskId)
      }
    }

    const isNewTaskExpanded = ref(false)

    const isExistingTaskExpanded = (taskId: string) => {
      return expandedTaskIds.value.has(taskId)
    }

    const addNewTask = async (): Promise<void> => {
      if (!newTask.value.title) return // Prevent adding empty tasks
      try {
        const addedTask = await addTask(newTask.value)
        tasks.value.push(addedTask) // Add the newly created task to the list
        // Reset new task input fields
        newTask.value = {
          title: '',
          description: '',
          due_date: new Date().toISOString().split('T')[0]
        }
        isNewTaskExpanded.value = false
      } catch (error) {
        console.error('Error adding task:', error)
      }
    }

    const saveTask = async (taskId: string) => {
      const task = tasks.value.find((t) => t.id === taskId)
      if (task) {
        await updateTask(task)
      }
    }

    const toggleComplete = async (taskId: string) => {
      const task = tasks.value.find((t) => t.id === taskId)
      if (task) {
        await completeTask(task)
      }
    }

    onMounted(() => {
      loadTasks()
    })

    return {
      addNewTask,
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
