from django.contrib.auth.models import User

from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.reverse import reverse
from employees import serializers

from employees.serializers import ProjectSerializer

from .permissions import IsObjectOwner, IsPM, IsAdmin

from employees.models import Employee, EmployeeInProject, Department, Project
from employees.serializers import EmployeeSerializer, DepartmentSerializer
# Create your views here.

@api_view(['GET'])
def home(request, format=None):
    return Response(
        {
            'departments': reverse('employees:department-list', request=request, format=format),
            'employees': reverse('employees:employee-list', request=request, format=format),
            'projects': reverse('employees:project-list', request=request, format=format),

        }
    )


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdmin]

    def perform_create(self, serializer):
        serializer.save()


class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdmin|IsObjectOwner]


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdmin]


class DepartmentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdmin]


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdmin|IsPM]

class ProjectDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdmin, IsPM]
