from django.contrib import admin
from .models import Employee, EmployeeInProject, Project, Department

# Register your models here.

admin.site.register([Employee, EmployeeInProject, Project, Department])