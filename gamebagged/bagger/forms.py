from django.forms import ModelForm
from .models import OrderPro

class BaggerOrderAcceptForm(ModelForm):
    class Meta:
        model = OrderPro
        fields = ['bagger']


class BaggerOrderUpdateForm(ModelForm):
    class Meta:
        model = OrderPro
        fields = ['bagger','status']