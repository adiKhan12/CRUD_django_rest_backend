
from django.shortcuts import render
import requests
# Create your views here.

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import Employees,Teams,Work_Arrangement
from .serializers import employeesSerializer,TeamsSerializer,WorkArrangementSerializer
from rest_framework import status
from rest_framework.response import Response


# Now understand we have datain database, eg. SQL database we need to convert the data type to json or html depends on use case
# There will be the time when we have to show the data from databse, add new data to database, update database or delete the entry from database
# Followinng are the classes and objects which will do this processes

# Sometimes there whould be some important information, so we can permit to only show that table in database no modification, no delete


class employeeList(APIView):
    # get method gets data from table (which is stored in database), serializer coverts it to json 
    def get(self,request):
        employee=Employees.objects.all()
        serialzier=employeesSerializer(employee,many=True)
        return Response(serialzier.data)
    

    # creating new data POST, Takes data and stores on new row
    def post(self,request):
        serializer=employeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    # updating data PUT to database
    def put(self,request,id=None):
        employee=Employees.objects.filter(id=id)
        serializer=employeesSerializer(employee,data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
    # delete the data from Employees
    def delete(self,request,id=None):
        employee=Employees.objects.filter(id=id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# same as above for different tables from database but concept is same
class TeamsList(APIView):
    def get(self,request):
        team=Teams.objects.all()
        serialzier=TeamsSerializer(team,many=True)
        return Response(serialzier.data)

    # taking the data
    def post(self,request):
        serializer=TeamsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class WorkTime(APIView):
    def get(self,request):
        workingtime=Work_Arrangement.objects.all()
        serialzier=WorkArrangementSerializer(workingtime,many=True)
        return Response(serialzier.data)
    

    # taking the data
    def post(self,request):
        serializer=WorkArrangementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    

# takes whatever data we have diaplyed at http://127.0.0.1:2090/employeelist. the datatype will be json. we try to render that data on the .html 
# the url for that html page is defined in EMP_app.urls.py
def dislay_data(request):
    response=requests.get("http://127.0.0.1:2090/employeelist")
    results=response.json()
    return render(request,"showdata.html",{"Employees":results })

