
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "due_date", "owner")  # 👈 Display these fields in the list view
    list_filter = ("status", "due_date" ,"owner")  # 👈 Add filtering options
    search_fields = ("title",)  # 👈 Enable searching by task title