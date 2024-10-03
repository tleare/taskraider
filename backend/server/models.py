import uuid

from django.db import models

class Task(models.Model):

    class TaskType(models.TextChoices):
        TODO = 'TODO', 'To-Do'
        DAILY='DAILY', 'Daily'
        HABIT='HABIT', 'Habit'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO: user_id
    title = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.CharField(max_length=5, choices=TaskType.choices, default=TaskType.HABIT)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title