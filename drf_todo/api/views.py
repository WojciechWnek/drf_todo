from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=["post"], parser_classes=[])
    def toggle_complete(self, request, pk=None):
        task = self.get_object()
        task.completed =not task.completed
        task.save()

        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)

