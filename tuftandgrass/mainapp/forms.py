from django import forms
from .models import OrderModel, SubscribeModel


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = [
            'name',
            'phone',
            'email',
            'text',
        ]


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribeModel
        fields = [
            'email',
        ]
