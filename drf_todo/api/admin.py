
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "owner")  # 👈 Display these fields in the list view
    list_filter = ("completed", "owner")  # 👈 Add filtering options
    search_fields = ("title",)  # 👈 Enable searching by task title