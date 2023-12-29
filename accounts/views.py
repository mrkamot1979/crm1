from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status = "Delivered").count()
    pending = orders.filter(status = "Pending").count()

    context = {'orders' : orders, 
               'customers' : customers,
               'total_orders' : total_orders,
               'delivered' : delivered,
               'pending' : pending,           
               }

   
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all() #this will gather all of the Products from the model
    return render(request, 'accounts/products.html', {'products' : products})

def customer(request, pk):
    customer = Customer.object.get(id=pk) #to get the specific Customer via Primar Key (pk)
    return render(request, 'accounts/customer.html')