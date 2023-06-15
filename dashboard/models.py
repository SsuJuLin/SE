from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    birthday = models.DateField(null=True)
    street = models.CharField(null=True, max_length=100)
    house_number = models.CharField(null=True, max_length=10)
    town = models.CharField(null=True, max_length=100)
    city = models.CharField(null=True, max_length=100)
    news_notification = models.BooleanField(default=False)
    activity_notification = models.BooleanField(default=False)
    promotion_notification = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username