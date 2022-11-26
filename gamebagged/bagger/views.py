from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
#
from django.views import View
#For models queries
from accounts.models import *
#forms
from .forms import BaggerOrderUpdateForm
#email
from django.core.mail import send_mail


def bagger(request, pk):
    bagger= User.objects.get(pk=pk)

    #all orders query
    orders = OrderPro.objects.all()
    #all customer query
    customer = OrderPro.objects.all()
    #total up customers
    total_customers = customer.count()
    #total orders
    total_orders = orders.count
    #delivered filter
    delievered = orders.filter(status='Delivered').count()
    #pending orders filter
    pending = orders.filter(status='Pending').count()

    # loop through the orders and add the price value, check if order is not shipped
    bagger_orders = []
    for order in orders:

        if not order.bagger:
            bagger_orders.append(order)


    context = {'orders':bagger_orders,
                'bagger':bagger,
                'customer':customer,
                'total_customers':total_customers,
                'total_orders' : total_orders,
                'delievered' : delievered,
                'pending' : pending
            }
            
    return render(request, 'bagger/bagger.html', context)


def bagupdateOrder(request, pk):
    order = OrderPro.objects.get(id=pk)

    form = BaggerOrderUpdateForm(instance=order)

    if request.method =='POST':
        form = BaggerOrderUpdateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('bagger/')

    context = {'form':form}

    return render(request, 'bagger/bagger_form.html', context)


def bagcancelOrder(request, pk):
    order = OrderPro.objects.get(id=pk)

    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'bagger/cancel_order.html', context)


def baggerhome(request, pk):

    #all orders query
    bagger = OrderPro.objects.get(pk=pk)
    orders = OrderPro.objects.filter(pk=pk)

    

    context = {'orders':orders,
                'bagger':bagger,
                
            }
            
    return render(request, 'bagger/baghome.html', context)