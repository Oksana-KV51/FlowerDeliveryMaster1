from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.catalog, name='catalog'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
]