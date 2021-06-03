from django.db import models

class User(models.Model):
    roll = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)