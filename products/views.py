from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    ''' a view that shows all products, and allows for searches of products'''

    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    '''
    a view that shows extra information about a product,
    '''
    
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_details.html', context)