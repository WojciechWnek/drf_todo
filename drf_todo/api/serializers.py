from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username"
        ]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            "title",
            'description',
            "completed",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        request = self.context.get("request")
        if request and request.user.is_superuser:
            owner_serializer = UserSerializer(instance.owner)
            data["owner"] = owner_serializer.data  # 👈 Add owner field for superusers

        return data
