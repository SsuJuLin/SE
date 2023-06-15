from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from datetime import datetime

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'birthday', 'street', 'house_number', 'town', 'city']

class NotificationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['news_notification', 'activity_notification', 'promotion_notification']