from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    Role_CHOICE = [
        ('user', 'User'),
        ('buyer', 'Buyer'),
        ('vendor', 'Vendor')
    ]

    role = models.CharField(max_length=10,
    choices=Role_CHOICE, default='user')

    def __str__(self):
        return f"{self.username} ({self.role})"

    def  is_user(self):
        return self.role == 'user'
    
    def is_buyer(self):
        return self.role =='buyer'
    
    def is_vendor(self):
        return self.role =='vendor'

