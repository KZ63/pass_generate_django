from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PassWord(models.Model):
      service_name = models.CharField(max_length=50)
      passWord = models.CharField(max_length=20)
      url = models.CharField(max_length=255)
      user_id = models.CharField(max_length=255)

class Account(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)

      last_name = models.CharField(max_length=100)
      first_name = models.CharField(max_length=100)
      account_image = models.ImageField(upload_to='profile_pics', blank=True)

      def __str__(self):
            return self.user.username