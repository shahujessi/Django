from django.shortcuts import render
from django.http import HttpResponse
from .product import Product

# Create your views here.
def home(request):
    products=Product.objects.all()
    return render(request, 'index.html', {'products':products})
