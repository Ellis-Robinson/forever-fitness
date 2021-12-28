'''
views and functions for all product related CRUD functionality
'''
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    ''' a view that shows all products, and allows for searches of products'''

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You havn't entered a search criteria")
                return redirect(reverse('products'))
            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query))
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories
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