# products/views.py
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.filter(active=True)
    return render(request, 'products/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    # Handle the logic for adding product to cart
    return render(request, 'products/cart.html')
