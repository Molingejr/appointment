# Appointment Reminder
This app reminds users of their scheduled appointments some minutes before the time through text message


## Installation
Install Python 3.6

Create a python virtual environment
```
python3.6 -m venv <env_name>
```
Install Dependencies
```
source venv/bin/activate
pip install -r requirements
```
Run migrations with 
```
python manage.py migrate reminder
```
Create superuser for admin account
```
python manage.py createsuperuser
```

Run the Application
```
python manage.py runserver
```

### Twilio Credentials
Go to **appointment/reminder/sms** and replace # Credentials for twilio account
ACCOUNT_SID, AUTH_TOKEN, SENDER_TEL with your twilio credentials

### Note
The Tel field of the schedule appointment form will require that you put your country code to the tel.
e.g. +14212215453