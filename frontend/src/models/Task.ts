export interface Task {
  id: string // UUID
  title: string
  description: string
  task_type: 'TODO' | 'DAILY' | 'HABIT'
  created_at: string // ISO string
  due_date: string // ISO string
  completed: boolean
}
