from django.shortcuts import render, redirect
#
from django.views import View
#For models queries
from .models import *
#forms
from .forms import OrderProForm, CustomerOrderUpdateForm
#email
from django.core.mail import send_mail

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
    context = {'orders':orders,
                'customers':customers,
                'total_customers':total_customers,
                'total_orders' : total_orders,
                'delievered' : delievered,
                'pending' : pending
            }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    #all products query
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'accounts/products.html', context)

def customer(request, pk):
    customer= OrderPro.objects.get(pk=pk)

    
    #query customer child object
    #from models field
    #orders
    orders = OrderPro.objects.filter(pk=pk)

    #count the orders
    orderpro_count = orders.count()

    context={
        'customer':customer,
        'orders' : orders,
        'orderpro_count' : orderpro_count,
    }
    return render(request, 'accounts/customer.html', context)

class PlaceOrder(View):
    def get(self, request,  *args, **kwargs):
        #get every item from each category
        vgs = Product.objects.filter(category__contains='Video Games')
        accs = Product.objects.filter(category__contains='Accessories')
        phones = Product.objects.filter(category__contains='Mobile Phones')
        systems = Product.objects.filter(category__contains='Consoles')

        form = OrderProForm()
        

        #pass into context
        context = {
                'vgs':vgs,
                'accs':accs,
                'phones':phones,
                'systems':systems,
                'form' : form,
                'products' : products,
            }

        #render the template
        return render(request, 'accounts/order.html', context)

    def post(self, request, *args, **kwargs):
        customer = request.POST.get('customer')

        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')
           #loop through and grab needed data/menu item from database and {id} 
        for item in items:
            #p=1(item) gets rid of muitlple items error
            item_for_sale = Product.objects.get(pk=int(item))
            #get price, id, and name
            item_data = {
                'id': item_for_sale.pk,
                'name': item_for_sale.name,
                'price': item_for_sale.price
            }

            #pin to items list
            order_items['items'].append(item_data)

            #calculate total data
            price = 0
            item_ids = []

        for item in order_items['items']:
            #total price
            price += item['price']
            item_ids.append(item['id'])

        order = OrderPro.objects.create(
            price=price,
            )

        order.items.add(*item_ids)

        context = {
            'items' : order_items['items'],
            'price' : price,
            'customer' : customer,
        }

        return render(request, 'accounts/orderconfirm.html', context)

def cusupdateOrder(request, pk):
    order = OrderPro.objects.get(id=pk)
    form = CustomerOrderUpdateForm(instance=order)

    if request.method =='POST':
        form = CustomerOrderUpdateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)


def cuscancelOrder(request, pk):
    order = OrderPro.objects.get(id=pk)
    context = {'item':order}
    return render(request, 'accounts/cancel_order.html', context)
