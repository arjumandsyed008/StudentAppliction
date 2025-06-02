from django import forms
from .models import StudentProfile, Application
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['date_of_birth', 'address']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['course']
