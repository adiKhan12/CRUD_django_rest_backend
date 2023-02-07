from django.test import TestCase
from .models import Teams,Employees,Work_Arrangement
# Create your tests here.


# Testin the API providing the input info

class employeestestcase(TestCase):
    def test_employee(self):
        team=Teams.objects.create(Add_Team="Team_test")
        self.assertEqual(str(team), 'Team_test')

class EmployeeTest(TestCase):
    def setup(self):
        self.team=Teams.objects.create(Add_Team="Team_test")
        
    def employee_test_repesentation(self):
        employee=Employees.objects.create(
            Full_Name="Test_employee",
            Employee_Id=19,
            Part_of_Team=self.team,
            Hourly_Rate=99,
            Team_Lead=True
        )
        self.assertEqual(str(employee),"Test_employee")

class Work_Time_Test(TestCase):

    def setUp(self):
        self.team=Teams.objects.create(Add_Team="Team_test")

    def work_time_test_employee_representation(self):
        self.employee=Employees.objects.create(
            Full_Name="Test_employee",
            Employee_Id=19,
            Part_of_Team=self.team,
            Hourly_Rate=99,
            Team_Lead=True
        )

    def workarrangementtest(self):
        work_time=Work_Arrangement.objects.create(
            employee=self.employee,
            is_full_time=False,
            is_part_time=True,
            WorkPercentage=40
        )
        self.assertEqual(work_time.employee,self.employee)
        


