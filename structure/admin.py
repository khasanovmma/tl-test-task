from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["full_name", "position", "employment_date", "parent"]
    search_fields = ["full_name", "position"]