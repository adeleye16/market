from django import forms
from django.forms import ModelForm
from . models import * 

class ContactForm(forms.ModelForm):
    class Meta:
      model = Contact
      fields = ['full_name', 'email', 'message']

      
class CartForm(forms.ModelForm):
  class Meta:
    model = Cart
    fields = ['quantity']
      
