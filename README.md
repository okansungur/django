# Django 
Django is one of the most popular Python web framework.Django provides a complete mechanism for managing database,templates,rest. We can define Django as a full-stack web framework, whereas Flask is a light-weight (micro) framework when compared.Although Django is a production-ready framework if the requirements change dynamically it is not preffered. Django is good for big projects whereas Flask for simple applications that dont require too much coding.
The Django has MVT(Model View Template) pattern 
- Model: Manages data and business.(Data Access Layer)
- View: Deals with the business logic and returns a response to the user by the help of a model to carry data to templates
- Presentation: Html, css, javascript and static files (presentation layer)
A Django project contains packages and files
 - manage.py : A command-line utility that executes Django-specific tasks
 - _init__.py: An empty file that tells Python to treat directories as a Python package
 - settings.py: Django application configurations are kept here.
 - urls.py: Contain listed URLs for the web application
 - wsgi.py:(Web Server Gateway Interface)Entry-point to serve Django project.



<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/python.png"><br/>
  Python
</p>
After downloading python. Check the python version from the commnand line.We will also need to install Django and Djangorest framework.
<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/django.png"><br/>
  Django
</p>


<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/djangorest.png"><br/>
  Rest
</p>

We will use PyCharm as the IDE as it provides lots of features for developers.

<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/project1.png"><br/>
  PyCharm
</p>

Create a project WebApp.
<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/myfirstapp.png"><br/>
  My_Web_Project
</p>

To keep code simple and clean  Django project vcan consist multiple applications. To create an application we will use the command __manage.py startup my_web_project__ command.


<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/createmy_web_proj.png"><br/>
  My_Web_Project
</p>

We will use a database SQLite,  where  we define in __settings.py__.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'MyDatabase'),
    }
}
```
 Then  We will create our tables by using __models.py__
 ```
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
```

<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/database.png"><br/>
  Embeded Database
</p>



With migration command we execute  SQL commands in the database file and all the tables of  installed apps are created in our database. You can check the migration folder after executing the command.
<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/django3.png"><br/>
  Migration
</p>

To add an initial data we added migrations.RunSQL command to our generated code __0001_initial.py__.


<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/myfirstapp2.png"><br/>
  
</p>



<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/myfirstapp3.png"><br/>
  
</p>


To dockerize the application We have to make some modifications. We changed ALLOWED_HOSTS parameter from the __settings.py__.
And we prepare a requirements.txt. This file  lists all of the modules needed for the Django project to work.
<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/dockerize1.png"><br/>
  Hosts Configuration
</p>

Dockerize the web application
```
docker run -p 8000:8000 greenredblue/mydjango:v1
```

<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/output.png"><br/>
  Web Project Output
</p>


Test the rest post method with Postman
<p align="center">
  <img  src="https://github.com/okansungur/django/blob/main/img/PostMethod.png"><br/>
  Testing post method
</p>


