from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
  # ('actual db value', 'admin value')
  STATUS = [
    ('new', 'new'),
    ('pending', 'pending'),
    ('updated', 'updated'),
    ('completed', 'completed'),

  ]
  full_name = models.CharField(max_length=50)
  email = models.EmailField()
  message = models.TextField()
  status = models.CharField(max_length=50,default= 'new', choices= STATUS)
  sent = models.DateField(auto_now= True)
  updated = models.DateField(auto_now_add= True)

  def _str_(self):
    return self.full_name

  class Meta:
    db_table = 'contact'
    managed = True
    verbose_name = 'Contact'
    verbose_name_plural = 'Contact'


class Category(models.Model):
  title = models.CharField(max_length=50)
  img = models.ImageField(upload_to= 'category', default= 'category.jpg')
  slug = models.SlugField(default= '-')

  def _str_(self):
    return self.title

class Product(models.Model):
  category = models.ForeignKey(Category,on_delete= models.CASCADE )
  title_r = models.CharField(max_length=50)
  slug = models.SlugField(default='-')
  img_r = models.ImageField(upload_to = 'product', default= 'product.jpg')
  description = models.TextField()
  price = models.FloatField()
  max_quantity = models.IntegerField()
  min_quantity = models.IntegerField()
  size = models.IntegerField()
  display = models.BooleanField()
  shoe = models.BooleanField()
  bags = models.BooleanField()
  perfume = models.BooleanField()
  cloth = models.BooleanField()
  uploaded = models.DateField(auto_now_add = True)

  def __str__(self):
    return self.title_r
  

class Cart(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
  product = models.ForeignKey(Product, on_delete= models.CASCADE)
  title_g  = models.CharField(max_length=50,null=True, blank=True, default='g')
  price = models.IntegerField()
  quantity = models.IntegerField()
  amount = models.IntegerField(null=True, blank=True)
  paid = models.BooleanField(default=False)
  order_no = models.CharField(max_length=60)
  payment_date = models.DateTimeField(auto_now_add = True)

  def __str__(self): 
    return self.product.title_r
  
  class Meta:
    db_table ='cart'
    managed = True
    verbose_name ='Cart'
    verbose_name_plural ='Cart'






