from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=127, blank=False, null=False)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):

    class EmployeeRole(models.TextChoices):
        DEFAULT = 'Default'
        PM = 'PM'
        ADMINISTRATOR = 'Administrator'

        def __str__(self):
            return self

    name = models.CharField(max_length=127, blank=False, null=False)
    surname = models.CharField(max_length=127, blank=False, null=False)
    login = models.CharField(max_length=127, blank=False, null=False)
    password = models.CharField(max_length=1023, blank=False, null=False)
    email = models.EmailField()
    employee_role = models.CharField(max_length=31, choices=EmployeeRole.choices, blank=False, null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    last_login_date = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.employee_role}"
    


class Project(models.Model):

    class ProjectStatuses(models.TextChoices):
        PLANNED = 'Planned'
        ONGOING = 'Ongoing'
        STOPPED = 'Stopped'

    description = models.TextField(blank=False, null=False)
    project_status = models.CharField(max_length=31, choices=ProjectStatuses.choices, blank=False, null=False)
    created_status = models.DateField(auto_now_add=True, blank=False, null=False)
    start_date = models.DateField(blank=True, null=True)
    stop_date = models.DateField(blank=True, null=True)


class EmployeeInProject(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=False, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=False, null=True)
