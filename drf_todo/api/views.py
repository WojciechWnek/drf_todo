from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        """Return only the tasks that belong to the logged-in user."""
        if self.request.user.is_superuser:
            return Task.objects.all()

        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["post"], parser_classes=[])
    def toggle_complete(self, request, pk=None):
        task = self.get_object()
        task.completed =not task.completed
        task.save()

        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)

