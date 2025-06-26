from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


#  Add project creation functionality
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['progress','title', 'description', 'due_date', 'priority', 'details']
        labels = {
            'details': 'Project Details',
        }
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
