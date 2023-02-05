from django.db import models

# Create your models here.
class PassWord(models.Model):
      service_name = models.CharField(max_length=50)
      passWord = models.CharField(max_length=20)
      url = models.CharField(max_length=255)