from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm
from django.utils.translation import gettext as _


# class SigninUserForm(ModelForm):
#     """The SignIn Form"""
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         error_messages = {
#             'username': {
#                 'unique': _('Enter another username. This one is taken')
#             }
#         }


class SigninUserForm(UserCreationForm):
    email = forms.EmailField(required=True)                                         # Adds the email field to the form and makes it a required field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
