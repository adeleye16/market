from django.db import models
from django.contrib.auth.models import User
from home.models import *

# Create your models here.
class Payment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  paid = models.BooleanField()
  amount = models.IntegerField()
  phone = models.CharField(max_length=45)
  pay_code = models.CharField(max_length=45)
  shop_code = models.CharField(max_length=45)
  payment_date = models.DateTimeField(auto_now=True)
  admin_update = models.DateTimeField(auto_now_add= True)
  admin_note = models.TextField()


  def __str__(self):
      return self.user.username
  
