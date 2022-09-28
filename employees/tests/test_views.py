from django.test import TestCase, Client
from django.urls import reverse, resolve
from employees.models import Employee, EmployeeInProject, Project, Department
import json


class TestView(TestCase):

    # def setUp(self):
    #     self.client = Client()
    #     self.home_url = reverse('employees:home')

    #     self.department1 = Department.objects.create(
    #         name='Department1',
    #     )

    #     self.employee1 = Employee.objects.create(
    #         name='Mateusz',
    #         surname='Wasielewski',
    #         login='foo',
    #         password='bar',
    #         email='greatmail@godel.com',
    #         employee_role='Default',
    #         salary=5500,
    #         department=Department.objects.get(pk=1),
    #     )

    #     self.details_url = reverse('employees:employee_details', args=[1])


    # def test_list_of_all_employees_GET(self):
    #     response = self.client.get(self.home_url)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'employees/home.html')

    # def test_employee_detail_GET(self):
    #     response = self.client.get(self.details_url)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'employees/employee.html')

    # def test_adding_employees_POST(self):
    #     self.add_employee = reverse('employees:add_employee')
    #     response = self.client.post(self.add_employee, {
    #         'name': 'Mateusz2',
    #         'surname': 'Wasielewskiii',
    #         'login': 'fooooo',
    #         'password': 'baaar',
    #         'email': 'm.was@gtech.com',
    #         'employee_role': 'Default',
    #         'salary': '1',
    #         'department': 'Department1'
    #     })
    #     self.assertEqual(response.status_code, 302)
