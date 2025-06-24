from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'is_pinned')
    list_filter = ('is_pinned',)
    search_fields = ('title',)
