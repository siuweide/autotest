from django.contrib import admin
from project.models import Project, Module

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'status', 'create_time']

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['project', 'name', 'describe', 'create_time']
