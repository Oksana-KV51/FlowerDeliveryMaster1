
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, OrderForm
from .models import Flower, Order

def register(request):# регистрация
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('catalog')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def catalog(request):# каталог
    flowers = Flower.objects.all()
    return render(request, 'catalog/catalog.html', {'flowers': flowers})

def add_to_cart(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, initial={'flower': flower})
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_confirmation')
        else:
            form = OrderForm(initial={'flower': flower})
    return render(request, 'add_to_cart.html', {'form': form, 'flower': flower})

def order_confirmation(request):
    return render(request, 'order_confirmation.html')
