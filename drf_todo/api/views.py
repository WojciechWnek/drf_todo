from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from .models import Task
from .serializers import TaskSerializer, TaskStatusUpdateSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        """Return only the tasks that belong to the logged-in user."""
        if self.request.user.is_superuser:
            return Task.objects.all()

        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(
        detail=True,
        methods=["post"],
        parser_classes=[MultiPartParser],
        serializer_class=TaskStatusUpdateSerializer
    )
    @extend_schema(request=TaskStatusUpdateSerializer)
    def update_status(self, request, pk=None):
        task = self.get_object()

        serializer = TaskStatusUpdateSerializer(data=request.data)
        if serializer.is_valid():
            new_status = serializer.validated_data["status"]
            task.status = new_status
            task.save()

            return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



