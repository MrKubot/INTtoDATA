from importlib.metadata import requires
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Employee, EmployeeInProject, Project, Department


class DepartmentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=127, allow_blank=False)
    created_date = serializers.DateField(read_only=True)

    def __str__(self) -> str:
        return self.name

class EmployeeSerializer(serializers.ModelSerializer):
    last_login_date = serializers.DateField(read_only=True)
    created_date = serializers.DateField(read_only=True)
    
    class Meta:
        model = Employee
        fields = ['name', 'surname', 'login', 'password', 'email', 
        'employee_role', 'salary', 'department', 'last_login_date', 'created_date']


# class EmployeeSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=127, allow_blank=False)
#     surname = serializers.CharField(max_length=127, allow_blank=False)
#     login = serializers.CharField(max_length=127, allow_blank=False)
#     password = serializers.CharField(max_length=1023, allow_blank=False)
#     email = serializers.EmailField()
#     employee_role = serializers.ChoiceField(choices=Employee.EmployeeRole)
#     salary = serializers.DecimalField(max_digits=10, decimal_places=2)
#     department = serializers.CharField()
#     last_login_date = serializers.DateTimeField(read_only=True)
#     created_date = serializers.DateField(read_only=True)

#     def create(self, data: dict):
#         return Employee.objects.create(**data)

#     def update(self, instance: Employee, data: dict):
#         instance.name = data.get('name', instance.name)
#         instance.surname = data.get('surname', instance.surname)
#         instance.login = data.get('login', instance.login)
#         instance.password = data.get('password', instance.password)
#         instance.employee_role = data.get('employee_role', instance.employee_role)
#         instance.email = data.get('email', instance.email)
#         instance.salary = data.get('salary', instance.salary)
#         instance.department = data.get('department', instance.department)
#         instance.save()

#         return instance

#     def __str__(self):
#         return f"Serialized {self.name} {self.surname} - {self.employee_role}"

