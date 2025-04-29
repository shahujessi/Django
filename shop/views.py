from django.shortcuts import render
from django.http import HttpResponse
from .product import Product
from .category import Category

# Create your views here.
def home(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    category_id=request.GET.get('category')
    if category_id:
        products=Product.objects.filter(category_id=category_id)
    else:
        products=Product.objects.all()
    data={'products':products, 'categories':categories}
    return render(request, 'index.html', data)

# Signup Form
def signup(request):
    return render(request, 'signup.html')