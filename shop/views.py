from django.shortcuts import render
from .models import Product, Category


def index(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})
