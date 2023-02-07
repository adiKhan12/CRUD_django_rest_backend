from django.db import models

# Create your models here.
from django.db import models


# create class to add innformationa and schemas
class Teams(models.Model):
  Add_Team=models.CharField(max_length=30)

  def __str__(self):
    return self.Add_Team


# this gives information about the all team employess
class Employees(models.Model):
  Full_Name=models.CharField(max_length=20)
  Employee_Id=models.PositiveIntegerField()
  Part_of_Team=models.ForeignKey(Teams,on_delete=models.CASCADE)
  Hourly_Rate=models.PositiveIntegerField()
  Team_Lead=models.BooleanField()

  def __str__(self):
    return self.Full_Name


# define about the working time freedom, to know who works how much 
class Work_Arrangement(models.Model):
  employee=models.ForeignKey(Employees,on_delete=models.CASCADE)
  is_full_time=models.BooleanField(default=False)
  is_part_time=models.BooleanField(default=True)
  WorkPercentage=models.FloatField(default=40)

  def __str__(self):
     return f"{self.employee} -- {self.is_part_time} -- {self.WorkPercentage}"
  
