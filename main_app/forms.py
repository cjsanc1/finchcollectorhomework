# forms.py

from django.forms import ModelForm
from .models import YourOrder

class OrderForm(ModelForm):
  class Meta:
    model = YourOrder
    fields = ['date', 'item']