how to make book_store works:

1- Clone this repo 

2- cd django

3- Create Virtual Environment

   for windows:
   
   py -m venv environment
   
4- Activate it

   for windows:
   
   environment\Scripts\activate.bat
   
   - You will find in cmd something like this
   
   (environment)C:\Users\DELL\Desktop\django_labs>
   
5- install django

   - py -m pip install Django
   
6- now enter the project

   - cd book_store
   
7- Install the mysqlclient package:

   - pip install mysqlclient

8- create database in phpmyadmin called "mydatabase"

9- change phpmyadmin details in settings.py to yours
  
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

10- python manage.py makemigrations

11- python manage.py migrate
   
12- Now it's time to run the project

  - py manage.py runserver
  
Sample Run:

![image](https://github.com/ahmedabdelrahim123/django/assets/48600143/e0860c2e-667a-428d-9662-1fa98f1a577b)

![image](https://github.com/ahmedabdelrahim123/django/assets/48600143/5839ccfa-daee-446e-b535-30714c6eefff)


