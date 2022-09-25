from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from employees.views import add_employee, EmployeeDetailView

class TestUrls(TestCase):

    def test_add_employee(self):
        url = reverse('employees:add_employee')
        self.assertEqual(resolve(url).func, add_employee)

    def test_employee_details(self):
        url = reverse('employees:employee_details', args=[4])
        self.assertEqual(resolve(url).func.view_class, EmployeeDetailView)