import json
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return render(request, 'mart/home.html' )

ORDERS_FILE = os.path.join(os.path.dirname(__file__), '..', 'data.json')
CART_FILE = os.path.join(os.path.dirname(__file__), '..', 'cart.json')

def list_items(request):
    if request.method == 'GET':
        if os.path.exists(ORDERS_FILE):
            with open(ORDERS_FILE, 'r') as file:
                orders = json.load(file)
        else:
            orders = []

        return render(request, 'mart/list_items.html', {'orders': orders})

def add_to_cart(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('items')  
        if os.path.exists(ORDERS_FILE):
            with open(ORDERS_FILE, 'r') as file:
                orders = json.load(file)
        else:
            orders = []


        cart = [order for order in orders if str(order.get('orderId')) in selected_items]

      
        with open(CART_FILE, 'w') as file:
            json.dump(cart, file, indent=4)

        return redirect('cart')

    return HttpResponse("Method Not Allowed", status=405)

def cart(request):
    if os.path.exists(CART_FILE):
        with open(CART_FILE, 'r') as file:
            cart_items = json.load(file)
    else:
        cart_items = []

    return render(request, 'mart/cart.html', {'cart_items': cart_items})