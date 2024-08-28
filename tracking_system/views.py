import json
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .utils import read_orders, add_order
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def list(request):
    orders = read_orders()
    return JsonResponse({"orders": orders})

@csrf_exempt
def add(request):
   if request.method == 'POST':
        data = json.loads(request.body)
        orderId = data.get('orderId')
        orderName = data.get('orderName')
        username = data.get('username')
        status = data.get('status')
        
        new_order = {
            'orderId': orderId,
            'orderName': orderName,
            'username': username,
            'status': status
        }
        add_order(new_order)
        return JsonResponse({"message":"order added "})
   
   return JsonResponse({"message": "http method not supported"})

def index(request):
    return JsonResponse({})