from django.contrib import admin

from models_demo.web.models import Employee, Departments

admin.site.register(Departments)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'id',)
