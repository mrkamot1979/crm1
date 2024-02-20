from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm #needs to be imported so that we can use it in the view below
 
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
    customer = Customer.objects.get(id=pk) #to get the specific Customer via Primar Key (pk)
    total_order = customer.order_set.all().count()
    orders = customer.order_set.all()

    context = {'customer' : customer, 
               'total_order' : total_order,
               'orders' : orders,
               }
    return render(request, 'accounts/customer.html', context)

#CRUD

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10) #arguments are Parent model (Customer), and Child model (Order)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer) #if we have objects there there, do not reference them, just show new/blank items.
    #form = OrderForm(initial={'customer' : customer}) #this populates the form with the pre-selected customer
    if request.method == 'POST': #whole process essentially returns the data back to the form and the form saves/processes the request
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = { 
        'formset' : formset
    }

    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk) #this line is used to get the specific order via the order ID
    form = OrderForm(instance=order) #populates the form with the data to be edited
    if request.method == 'POST': #whole process essentially returns the data back to the form and the form saves/processes the request
        form = OrderForm(request.POST, instance=order) #dont forget the "instance=order" to update the instance
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    context = {
        'item' : order
    }
    return render(request, 'accounts/delete.html', context)


    