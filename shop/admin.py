from django.contrib import admin
from .product import Product
from .category import Category

# Register your models here.
class Categoryinfo(admin.ModelAdmin):
    list_display=["name"]

class Productinfo(admin.ModelAdmin):
    list_display=["name","category","price"]

admin.site.register(Product,Productinfo)
admin.site.register(Category,Categoryinfo)