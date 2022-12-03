import django_filters

from accounts.models import OrderPro

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = OrderPro
        fields = ['bagger']
