from django.contrib import admin

from CBViews_demo.web.models import Employee, Departments, Photo

admin.site.register(Departments)

admin.site.register(Photo)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'id',)
