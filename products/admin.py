# products/admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'active', 'image')
    list_filter = ('active',)
    search_fields = ('name',)
