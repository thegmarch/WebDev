from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=264,unique=False)
    last_name = models.CharField(max_length=264,unique=False)
    usr_email = models.EmailField(max_length=264,unique=True)
