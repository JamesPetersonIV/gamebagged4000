from django.urls import path
from . import views
#HTTP
#from django.http import HttpResponse
from accounts.views import PlaceOrder, Accessories, Phones, VideoGames, Consoles, VideoGamesSearch, ConsolesSearch, AccessoriesSearch, PhonesSearch
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('products/', views.products, name='products'),
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('order/', PlaceOrder.as_view(), name='order'),
    path('update_order/<int:pk>/', views.cusupdateOrder, name='update_order'),
    path('cancel_order/<int:pk>/', views.cuscancelOrder, name='cancel_order'),
    #category lists
    path('category/accs/', Accessories.as_view(), name='accs' ),
    path('category/accs/search/', AccessoriesSearch.as_view(), name='accs-search'),

    path('category/phones/', Phones.as_view(), name='mps' ),
    path('category/phones/search/', PhonesSearch.as_view(), name='mps-search'),

    path('category/consoles/', Consoles.as_view(), name='cons' ),
    path('category/consoles/search/', ConsolesSearch.as_view(), name='gs-search'),

    path('category/games/', VideoGames.as_view(), name='games' ),
    path('category/games/search/', VideoGamesSearch.as_view(), name='vgs-search'),
] 