from django.shortcuts import render,redirect
from django.http import HttpResponse
from .product import Product
from .category import Category
from django.contrib.auth.hashers import make_password,check_password
from .customer import Customer



# Signup Form
def signup(request):
    if request.method=='GET':
        return render(request, 'signup.html')
    else:
        
#login page
def login(request):
    

#login page
def login(request):
    if request.method=='GET':
        return render(request, 'login.html')
    else:
        
        