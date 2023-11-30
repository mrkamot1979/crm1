from django.contrib import admin

# Register your models here.

#lines below are needed to register the Customer database in the Admin panel
from .models import Customer
admin.site.register(Customer) 
