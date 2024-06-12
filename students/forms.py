from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'age', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter the Student Name', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter the Student Email', 'required': 'required'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Enter the Student Age', 'required': 'required'}),
            'gender': forms.Select(attrs={'required': 'required'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'age': 'Age',
            'gender': 'Gender',
        }
