from django import forms
from .models import User, NotificationSettings

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthday', 'street', 'house_number', 'town', 'city']

class NotificationForm(forms.ModelForm):
    class Meta:
        model = NotificationSettings
        fields = ['news_notification', 'activity_notification', 'promotion_notification']