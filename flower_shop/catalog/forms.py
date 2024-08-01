from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Order

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['flower', 'quantity', 'delivery_address']