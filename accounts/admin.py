from django.contrib import admin

# Register your models here.

#lines below are needed to register the Customer database in the Admin panel
from .models import Customer, Product, Order
admin.site.register(Customer) 
admin.site.register(Product) 
admin.site.register(Order) 
