from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.list_items, name='list_items'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
]
