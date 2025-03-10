# Generated by Django 5.1.7 on 2025-03-10 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_task_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('In Progress', 'In Progress'), ('Done', 'Done')], default='Todo', max_length=12),
        ),
    ]
