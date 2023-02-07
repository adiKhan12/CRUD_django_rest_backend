from django.contrib import admin
from .models import Employees,Work_Arrangement,Teams

# Register your models here.
admin.site.register(Employees)
admin.site.register(Work_Arrangement)
admin.site.register(Teams)