from django.contrib import admin
from . import models


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'school_motto', 'school_type', \
        'school_logo', 'school_address', 'school_phone', 'school_website']
    index_title = 'Welcome to Admin Page'
    site_header = 'School Administration Interface'
    site_title = 'School Album System'

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'school', 'dob', 'gender', 'state']
    list_filter = ['first_name', 'school', 'state']
    list_select_related = ['school']