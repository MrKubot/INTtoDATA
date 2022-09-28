from dataclasses import field
from importlib.metadata import requires
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee, EmployeeInProject, Project, Department


class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=127, allow_blank=False)

    class Meta: 
        model = Department
        fields = ['id', 'name', 'create_date']

    def __str__(self) -> str:
        return self.name

class EmployeeSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        employee = Employee.objects.create_user(
            username=validated_data['username'],
            name=validated_data['name'],
            surname=validated_data['surname'],
            login=validated_data['login'],
            password=validated_data['password'],
            email=validated_data['email'],
            employee_role=validated_data['employee_role'],
            salary=validated_data['salary'],
            department=validated_data['department'],
        )
        
        return employee

    class Meta:
        model = Employee
        fields = ['id','username', 'name', 'surname', 'login', 'password', 
                  'email','employee_role', 'salary', 'department', 
                  'last_login_date', 'created_date']

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'description', 'project_status', 'created_status', 'start_date', 'stop_date']

    
