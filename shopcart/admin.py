from django.contrib import admin
from . models import *

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
  list_display = ['id', 'user', 'first_name', 'last_name', 'paid', 'amount', 'phone', 'pay_code', 
  'shop_code', 'payment_date', 'admin_update', 'admin_note']
admin.site.register(Payment, PaymentAdmin)