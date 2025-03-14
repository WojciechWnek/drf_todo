from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return f"{self.id} - {self.name}"


class Task(models.Model):
    class StatusChoices(models.TextChoices):
        TODO = "Todo"
        IN_PROGRESS = "In Progress"
        DONE = "Done"
        OVERDUE = "Overdue"


    title = models.CharField(max_length=200)
    description =models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    due_date = models.DateField()
    status = models.CharField(
        max_length=12,
        choices=StatusChoices.choices,
        default=StatusChoices.TODO,
    )

    def save(self, *args, **kwargs):
        if self.status not in [self.StatusChoices.DONE, self.StatusChoices.OVERDUE]:
            if self.due_date < timezone.now().date():
                self.status = self.StatusChoices.OVERDUE

        super().save(*args, **kwargs)


