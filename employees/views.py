from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, get_list_or_404
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import JsonResponse, HttpResponse

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from employees.models import Employee, EmployeeInProject, Department, Project
from employees.serializers import EmployeeSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def employee_list_or_add(request):
    if request.method == 'GET':
        employees = Employee.objects.all()

        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def employee_details(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class HomeView(generic.ListView):
#     template_name = 'employees/home.html'

#     def get_queryset(self):
#         return Employee.objects.all()


# class EmployeeDetailView(generic.DetailView):
#     model = Employee
#     template_name = 'employees/employee.html'


# def add_employee(request):
#     if request.method == "POST":
#         # django won't accept department as plain string - it needs to be instance of an class
#         department_instance = Department.objects.get(name=request.POST['department'])
#         salary_float = float(request.POST['salary'])

#         print(f"{request}0000000000000000000000000000000000")

#         new_employee = Employee(
#             name=request.POST['name'], 
#             surname=request.POST['surname'], 
#             login=request.POST['login'],
#             password=request.POST['password'], 
#             email=request.POST['email'], 
#             employee_role=request.POST['employee_role'], 
#             salary=salary_float,
#             department=department_instance)

#         new_employee.save()
#         return HttpResponseRedirect(reverse('employees:home'))
#     else:
#         content = {
#             'Departments': get_list_or_404(Department),
#             'Roles': Employee.EmployeeRole.choices,
#         }
#         return render(request, 'employees/add_employee.html', context=content)