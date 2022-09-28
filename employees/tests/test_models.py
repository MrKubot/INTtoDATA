import email
from unicodedata import name
from django.test import TestCase
from ..models import Employee, Project, EmployeeInProject, Department
import datetime


# Create your tests here.

class EmployeeModelTests(TestCase):
    
    # available_roles = [tuple_[0] for tuple_ in Employee.EmployeeRole.choices]

    # IMPORTANT! __new__() and other magic methods

    def setUp(self):
        self.new_INcorrect_employee = Employee.objects.create(
            name='foo',
            surname='bar',
            login='spam',
            password='spam',
            email='foo@bar.com',
            employee_role='king',
            salary=123
            )

        self.new_correct_employee = Employee.objects.create(name='foo', 
            surname='bar', 
            login='spam', 
            password='spam', 
            email='foo@bar.com', 
            employee_role='Default', 
            salary=123
            )


    # def test_false_employee_role_as_specified(self):
    #     self.assertFalse(self.new_INcorrect_employee.employee_role in self.available_roles)

    # def test_false_employee_date_of_created(self):
    #     self.assertEqual(self.new_INcorrect_employee.created_date, datetime.date.today())


    # def test_true_employee_role_as_specified(self):
    #     self.assertTrue(self.new_correct_employee.employee_role in self.available_roles)

    # def test_true_employee_date_of_created(self):
    #     self.assertEqual(self.new_correct_employee.created_date, datetime.date.today())