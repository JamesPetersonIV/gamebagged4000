from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('bagger/<int:pk>/', views.bagger, name='bagger'),
    path('bagger_order/<int:pk>/', views.bagacceptOrder, name='bagger_order'),
    path('baggeru_order/<int:pk>/', views.bagupdateOrder, name='baggeru_order'),
    path('baghome/<int:pk>/', views.baggerhome, name='baghome'),
] 