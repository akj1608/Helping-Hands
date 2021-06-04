from django.db import models

# Create your models here.

class SignUp(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    phone = models.IntegerField(default=0)
