from django.contrib import admin
from api.models import TaskList,Task

admin.site.register(Task)
admin.site.register(TaskList)
# @admin.register(TaskList)
# class TasklistAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'created_by')

