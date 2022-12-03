from django.shortcuts import render, redirect
#
from django.views import View
#For models queries
from accounts.models import *
from admininterface.forms import ThreadForm, ChatForm
from .models import ThreadModel, MessageModel
#
from django.db.models import Q
#email
from django.core.mail import send_mail
#login auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#
from bagger.decorators import allowed_users
#count 
from django.db.models import Count, Sum

#send to login url
@login_required(login_url='account_login')
@allowed_users(allowed_roles=['admins'])
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
    #delieveries by driver
    bagger = OrderPro.objects.values('bagger').filter(status='Delivered').annotate(orderpro_count=Count('bagger'))
    #search filter
    
    context = {
                'orders':orders,
                'customers':customers,
                'total_customers':total_customers,
                'total_orders' : total_orders,
                'delievered' : delievered,
                'pending' : pending,
                'bagger':bagger,
            }

    return render(request, 'admininterface/dashboard.html', context)

###view login
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'admininterface/index.html')


class ListThreads(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        #show thread to both users using filter
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context = {
            'threads':threads
        }

        return render(request, 'admininterface/chat.html', context)

class CreateThread(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()

        context = {
            'form':form,
        }
        return render(request, 'admininterface/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        #get data from form post request
        form = ThreadForm(request.POST)
        #username gets form username
        username = request.POST.get('username')
        #check if user exists without error(i.e try)
        try:
            #find thread that matches reciever user
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                #get thread;[0] first one in list
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                #redirect to thread
                return redirect('thread', pk=thread.pk)
            #find thread that matches reverse
            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                #if exists do the opposite
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)

            if form.is_valid():
                thread = ThreadModel(
                    user=request.user, 
                    receiver=receiver,
                )
                thread.save()

                return redirect('thread', pk=thread.pk)
        #if user does not exist
        except:
            return redirect('create-thread')

class ThreadView(LoginRequiredMixin,View):
    def get(self, request, pk, *args, **kwargs):
        form = ChatForm()
        thread = ThreadModel.objects.get(pk=pk)
        #get thread object pk from line above
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
            'thread':thread,
            'form': form,
            'message_list': message_list,
        }

        return render(request, 'admininterface/thread.html', context)

class CreateMessage(LoginRequiredMixin,View):
    def post(self, request, pk, *args, **kwargs):
        #get thread from url
        thread = ThreadModel.objects.get(pk=pk)
        #checking who is receiver
        #if current user set
        #if not vise versa
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver
        
        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message'),
        )

        message.save()
        return redirect('thread', pk=pk)