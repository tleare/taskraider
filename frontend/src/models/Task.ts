export interface Task {
  id: string // UUID
  title: string
  description: string
  created_at: string // ISO string
  due_date: string // ISO string
  completed: boolean
}
