from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "title", "description", "created_at", "due_date", "completed"]
