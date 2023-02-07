# Company Employee Management System(EMS) using django REST Framework

Company EMS is the basic example using django and django REST framework. 

1. Create virtual env: virtualenv create name_of_env and activate it name_of_env/Scripts/activate.ps1.
2. Install django: pip install django , pip install djangorestframework and get started with company Emloyee Management System.
3. Start project: djangi-admin startproject name_of_project
4. Change the work directory cd name_of_project, create new app: pip manage.py startapp name_of_app
5. add the name of app to setting.py. add "rest_framework", "name_of_app"

Once this is done check the different folder and .py files created in the main folder.
These are the basic steps which must be followed

I have created 3 Models in models.py such as Teams, Employees, Work_Arrangement. The field (schema or type or datatype) are defined in models.py. Once These are defined 
use python manage.py createsuperuser then enter username, email and password.

Run following commands to migrate chnages
python manage.py makemigrations
python manage.py migrate
python manage.py runserver or python manage.py runserver "port number" eg. python manage.py runserver 5000  which will open url like this http://127.0.0.1:5000


Create serializer.py
folder of name_of_app where I have defined the serializer.

Let dicuss what is serializer.

Why do we need serializer?
Consider the datatype of data from database, if we want to covert this datatype to json or html we use serializer or When we try to create new record in database using POST, it is very
important to convert datatype of data which is create to datatype of database format. for this purpose serializer are used.
The serializers are used to covert datatype to json or from json. In serializer.py we define the field we want to display.

define api view in views.py. Where we define GET, POST, PUT, DELETE 

GET: used to get data from table from database then convert datatype using serializer provide response, on calling GET.

POST: save way save data to the database

PUT: update data from database

delete: delete the record from database


Define the urls in name_of_project.urls.py whcih will help to show corrosponding view.

In admin.py register models which are created in models.py. enter admin.site.register(model_name) in models.py

Following things can be done:
a. The data we have show/displayed using GET (in views.py) on corrosponding url (name_of_project.urls.py), we can display that data on web page using html (need to define urls in name_of_project.urls.py).
This data can be displayed in table format using .html( I have defined show.html, where I have displayed the data being displayed using GET)

b. Opeations can be performed on Field from mdoels.py, results can be stored in new field. which can be dipalyed on show.html

Tesing the API: 
test.py used for testing the the django rest, different tests are created. python manage.py test is used to perfomr the tests







