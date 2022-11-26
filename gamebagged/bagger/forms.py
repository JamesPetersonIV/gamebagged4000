from django.forms import ModelForm
from .models import OrderPro

class BaggerOrderUpdateForm(ModelForm):
    class Meta:
        model = OrderPro
        fields = ['bagger']