from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models.product import Product
from shop.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from shop.models.customer import Customer
from django.views import View


#class based view
class home(View):
    def get(self,request):
        categories=Category.objects.all()
        category_id=request.GET.get('category')
        if category_id:
            products=Product.objects.filter(category_id=category_id)
        else:
            products=Product.objects.all()
        data={'products':products, 'categories':categories}
        return render(request, 'index.html', data)



    def post(self,request):
        pass