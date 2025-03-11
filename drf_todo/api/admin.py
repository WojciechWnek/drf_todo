
from django.contrib import admin
from .models import Task, Project

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "due_date", "owner", "project")  # 👈 Display these fields in the list view
    list_filter = ("status", "due_date" ,"owner")  # 👈 Add filtering options
    search_fields = ("title",)  # 👈 Enable searching by task title


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")  # 👈 Display these fields in the list view
    list_filter = ["owner"]  # 👈 Add filtering options
    search_fields = ("name",)  # 👈 Enable searching by task title