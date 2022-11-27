from django.shortcuts import render
#
from django.views import View
#For models queries
from accounts.models import *

#email
from django.core.mail import send_mail
#
from django.contrib.auth.decorators import login_required


#send to login url
@login_required(login_url='account_login')
def home(request):
    #all orders query
    orders = OrderPro.objects.all()
    #all customer query
    customers = User.objects.all()
    #total up customers
    total_customers = customers.count()
    #total orders
    total_orders = orders.count
    #delivered filter
    delievered = orders.filter(status='Delivered').count()
    #pending orders filter
    pending = orders.filter(status='Pending').count()
    #Category sales 


    context = {
                'orders':orders,
                'customers':customers,
                'total_customers':total_customers,
                'total_orders' : total_orders,
                'delievered' : delievered,
                'pending' : pending,
            }

    return render(request, 'admininterface/dashboard.html', context)


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'admininterface/index.html')
