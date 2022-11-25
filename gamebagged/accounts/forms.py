from django.forms import ModelForm
from .models import OrderPro

class OrderProForm(ModelForm):
    class Meta:
        model = OrderPro
        fields = ['customer']

class CustomerOrderUpdateForm(ModelForm):
    class Meta:
        model = OrderPro
        fields = ['items']