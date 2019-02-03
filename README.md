# Appointment Reminder
This app reminds users of their scheduled appointments some minutes before the time through text message


## Installation
Install Python 3.6

Create a python virtual environment
 ```
 python3.6 -m venv <env_name>
 ```
Run migrations with 
```
python manage.py makemigrations reminder
python manage.py migrate reminder
```
Create superuser for admin account
```
python manage.py createsuperuser
```