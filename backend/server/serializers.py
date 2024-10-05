from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Task, TaskCompletion


class TaskSerializer(ModelSerializer):
    completed = SerializerMethodField()
    class Meta:
        model = Task
        fields = ["id", "title", "description", "created_at", "due_date", "completed"]

    def get_completed(self, obj):
        return TaskCompletion.objects.filter(task=obj).exists()

class TaskCompletionSerializer(ModelSerializer):
    class Meta:
        model = TaskCompletion
        fields = ["id", "task", "completed_at"]