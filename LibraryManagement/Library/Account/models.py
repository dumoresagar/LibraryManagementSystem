from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Register(models.Model):
    mail=models.EmailField()
    username=models.CharField(max_length=32)