from rest_framework import serializers
from .models import Employees,Teams,Work_Arrangement

# fields contain information about which field to show 

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=("Full_Name","Team_Lead")

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teams
        fields=("Add_Team")

class WorkArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Work_Arrangement
        fields=("employee","is_part_time","WorkPercentage")


