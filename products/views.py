'''
views and functions for all product related CRUD functionality
'''
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from profiles.models import UserProfile
from wishlist.models import Wishlist, WishListItem
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    ''' a view that shows all products, and allows for searches of products'''

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        users_wishlist = Wishlist.objects.filter(profile=user_profile)
        wishlist_items = WishListItem.objects.all()
        users_wishlist_items = wishlist_items.filter(wishlist=users_wishlist[0])
        item_list = []
        # creates list of items in users wishlist
        for item in users_wishlist_items:
            item_list.append(item.product)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        users_wishlist = Wishlist.objects.filter(profile=user_profile)
        wishlist_items = WishListItem.objects.all()
        users_wishlist_items = wishlist_items.filter(wishlist=users_wishlist[0])
        item_list = []
        # creates list of items in users wishlist
        for item in users_wishlist_items:
            item_list.append(item.product)

        context = {
            'products': products,
            'search_term': query,
            'current_categories': categories,
            'current_sorting': current_sorting,
            'wishlist': item_list
        }
    else:
        context = {
            'products': products,
            'search_term': query,
            'current_categories': categories,
            'current_sorting': current_sorting,
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


@login_required
def add_product(request):
    ''' Add product to database '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product successfully added.')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Is the form valid?')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    ''' update product in database '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully updated.')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Is the form valid?')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'you are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    ''' Delete a product from database '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":

        product.delete()
        messages.success(request, 'Product deleted')

        return redirect(reverse('products'))

    else:
        template = 'products/delete_product.html'
        context = {
            'product': product,
        }
        return render(request, template, context)
