from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = ('deadline_date', 'create_date', 'text', 'status')


admin.site.register(Task, TaskAdmin)
