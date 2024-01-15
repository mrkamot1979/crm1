from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta: #specify at least 2 fields
        model = Order
        fields = '__all__' #specifies all of the fields.add()
        


