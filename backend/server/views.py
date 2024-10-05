from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Task, TaskCompletion
from .serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['POST'])
    def complete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if TaskCompletion.objects.filter(task=task).exists():
            TaskCompletion.objects.filter(task=task).delete()
        else:
            TaskCompletion.objects.create(task=task)
        return Response(status=status.HTTP_200_OK)
