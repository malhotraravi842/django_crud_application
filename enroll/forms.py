from django import forms
from django.forms import fields
from .models import User
from django.core import validators

class StudentRegistration(forms.ModelForm):

    class Meta:
        model = User
        fields = ['roll','name', 'email']
        widgets = {
            'roll': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }
