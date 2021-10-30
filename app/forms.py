from django.db import models
from django import forms
# from .models import Student
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# class StudentLoginForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['matric_no', 'surname']

#         

user = get_user_model()
class SigninForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20)


    def clean_username(self):
        user_username = user.objects.get(username=username)

        if user_username.exist():
            raise ValidationError('This username already exist!!')


