"""
Setup models for Admin screen
"""
from django.contrib import admin
from api.models.product import Product

# Register your models here.
admin.site.register(Product)
