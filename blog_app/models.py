# Create your models here.
# myapp/models.py

from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  # Store password as a hash in production

    def __str__(self):
        return self.username
