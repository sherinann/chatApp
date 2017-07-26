from django.db import models
from django.contrib import auth
from django.utils import timezone
# Create your models here.
#class User(models.Model):
  #  name=models.CharField(max_length=200)

class UserMessageInfo(models.Model):
    sender=models.CharField(max_length=200)
    receiver=models.CharField(max_length=200)
    time_of_message=models.DateTimeField(default=timezone.now())
    message=models.CharField(max_length=500)
    class Meta:
        order_with_respect_to='time_of_message'

    #def __str__(self):
   #     field_values= []


class ChatList(models.Model):
    #should be present in Users, set foreignkey
    name_user=models.CharField(max_length=200)

