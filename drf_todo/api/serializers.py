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
            "due_date",
            "status",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        request = self.context.get("request")
        if request and request.user.is_superuser:
            owner_serializer = UserSerializer(instance.owner)
            data["owner"] = owner_serializer.data

        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Exclude "Overdue" status for both creating and updating
        self.fields["status"].choices = [
            (key, label) for key, label in Task.StatusChoices.choices if key != Task.StatusChoices.OVERDUE
        ]

class TaskStatusUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Task.StatusChoices.choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Exclude "Overdue" status for both creating and updating
        self.fields["status"].choices = [
            (key, label) for key, label in Task.StatusChoices.choices if key != Task.StatusChoices.OVERDUE
        ]