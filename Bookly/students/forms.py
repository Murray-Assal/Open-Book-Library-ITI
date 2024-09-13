from students.models import *
# from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StudentForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'profileImage']
 



class RegistrationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone', 'address', 'profileImage', 'is_superuser']
