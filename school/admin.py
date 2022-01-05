from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'school_motto', 'school_type', \
        'school_logo', 'school_address', 'school_phone', 'school_website']

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']