from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'employees'

urlpatterns = [
    path('employees/', views.EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetails.as_view(), name='employee-details'),
    path('departments/', views.DepartmentList.as_view(), name='department-list'),
    path('departments/<int:pk>/', views.DepartmentDetails.as_view(), name='department-details'),
    path('projects/', views.ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetails.as_view(), name='project-details'),
    path('', views.home),
]

urlpatterns = format_suffix_patterns(urlpatterns)