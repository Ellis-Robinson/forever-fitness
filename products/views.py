from django.shortcuts import render
from .models import Product

def all_products(request):
    ''' a view that shows all products, and allows for searches of products'''
    
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)