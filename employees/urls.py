from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'employees'

urlpatterns = [
    path('employees/<pk>', views.employee_details),
    path('employees/', views.employee_list_or_add),
]

# urlpatterns = [
#     path('employee/add_employee/', views.add_employee, name='add_employee'),
#     path('employee/<pk>/', views.EmployeeDetailView.as_view(), name='employee_details'),
#     path('', views.HomeView.as_view(), name='home'),
    
# ]