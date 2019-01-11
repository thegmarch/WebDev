from django.db import models
from djano.forms import ModelForm
# Create your models here.

class SignUpForm(ModelForm):
    class Meta:
        fields = ['name','email']
        
