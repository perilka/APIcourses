from django.contrib import admin
from . import models

@admin.register(models.University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

    def short_description(self, obj):
        return (obj.description[:30] + '...') if len(obj.description) > 30 else obj.description
    short_description.short_description = "Description"

@admin.register(models.UniversityCourse)
class UniversityCourseAdmin(admin.ModelAdmin):
    list_display = ['university', 'course', 'semester', 'duration_weeks']