from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('home/', views.home, name="home"),
    path('', Index.as_view(), name='index'),
    #chat
    path('chat/', ListThreads.as_view(), name='chat'),
    path('chat/create-thread/', CreateThread.as_view(), name='create-thread'),
    path('chat/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('chat/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
] 