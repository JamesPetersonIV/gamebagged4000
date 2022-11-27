from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('home/', views.home, name="home"),
    path('', Index.as_view(), name='index'),
] 