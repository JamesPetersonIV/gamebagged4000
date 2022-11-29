from django.shortcuts import render, redirect
#
from django.views import View
#For models queries
from .models import *
#forms
from .forms import OrderProForm, CustomerOrderUpdateForm
#email
from django.core.mail import send_mail
#
from django.contrib.auth.decorators import login_required

@login_required(login_url='account_login')
def products(request):
    #all products query
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'accounts/products.html', context)

@login_required(login_url='account_login')
def customer(request, pk):
    #all orders query
    #orders = OrderPro.objects.all()
    customer = User.objects.get(pk=pk)
    #customer = getOrderIfOrderExistForCurrentCustomer(pk)
    orders = OrderPro.objects.filter(customer=pk)
    ordercount = orders.filter(status='Delivered').count()
    context={
        'customer':customer,
        'orders' : orders,
        'ordercount' : ordercount,
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
        
        form = OrderProForm(request.POST)
        customer = request.POST.get('customer')
        #customer = User.objects.all()
        #form = OrderProForm(initial={'customer':customer})
        #if request.method == 'POST':
            #form = OrderProForm(request.POST)
            #if form.is_valid():
                #form.save()

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
            customer_id=customer,
            )

        order.items.add(*item_ids)

        context = {
            'items' : order_items['items'],
            'price' : price,
            'form':form,
        }

        return render(request, 'accounts/orderconfirm.html', context)


@login_required(login_url='account_login')
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


@login_required(login_url='account_login')
def cuscancelOrder(request, pk):
    order = OrderPro.objects.get(id=pk)

    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/cancel_order.html', context)


#################################################################
class Phones(View):
    def get(self, request, *args, **kwargs):
        phones = Product.objects.filter(category__contains='Mobile Phones')
        context = {'phones':phones}
        return render(request, 'accounts/mobilephones.html', context)

class Phones(View):
    def get(self, request, *args, **kwargs):
        phones = Product.objects.filter(category__contains='Mobile Phones')
        context = {'phones':phones}
        return render(request, 'accounts/mobilephones.html', context)


class Accessories(View):
    def get(self, request, *args, **kwargs):
        accs = Product.objects.filter(category__contains='Accessories')
        context = {'accs':accs}
        return render(request, 'accounts/accessories.html', context)


class Consoles(View):
    def get(self, request, *args, **kwargs):
        systems = Product.objects.filter(category__contains='Consoles')
        context = {'systems':systems}
        return render(request, 'accounts/consoles.html', context)


class VideoGames(View):
    def get(self, request, *args, **kwargs):
        vgs = Product.objects.filter(category__contains='Video Games')
        context = {'vgs':vgs}
        return render(request, 'accounts/videogames.html', context)

def getOrderIfOrderExistForCurrentCustomer(pk):
    try:
        return OrderPro.objects.get(pk=pk)
    except OrderPro.DoesNotExist:
        return None