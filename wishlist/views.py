''' stores all functions for wishlist app '''
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from products.models import Product

from .models import Wishlist, WishListItem


@login_required
def wishlist(request):
    ''' loads/creates users wishlist page '''

    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        new_wishlist = Wishlist(name=user_profile, profile=user_profile)
        new_wishlist.save()

        users_wishlist = Wishlist.objects.filter(profile=user_profile)
        items = WishListItem.objects.all()
        users_items = items.filter(wishlist=users_wishlist[0])

    else:
        users_wishlist = Wishlist.objects.filter(profile=user_profile)
        items = WishListItem.objects.all()
        users_items = items.filter(wishlist=users_wishlist[0])

    template = 'wishlist/wishlist.html'
    context = {
        'user': user_profile,
        'wishlist': users_wishlist,
        'items': users_items,
        'on_wishlist': True
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    '''
    creates new wishlistitem connected to users wishlist
    '''

    user_profile = get_object_or_404(UserProfile, user=request.user)
    users_wishlist = Wishlist.objects.filter(profile=user_profile)
    wishlist_items = WishListItem.objects.all()
    users_wishlist_items = wishlist_items.filter(wishlist=users_wishlist[0])

    product = Product.objects.get(pk=product_id)
    item_list = []

    # creates list of items in users wishlist
    for item in users_wishlist_items:
        item_list.append(item.product)

    # checks if chosen product is already in users wishlist
    if product in item_list:
        messages.success(request, 'Product already in your wishlist.')
    else:
        # creates new instance of WishListItem with product and users profile
        new_wishlist_item = WishListItem(wishlist=users_wishlist[0],
                                         product=product)
        new_wishlist_item.save()
        messages.success(request,
                         'Product successfully added to your wishlist.')

    return redirect(reverse('products'))


@login_required
def remove_from_wishlist(request, product_id):
    ''' deletes wishlistitem and returns to products view'''

    # gets wishlist item with users profile and product id
    product = Product.objects.get(pk=product_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    users_wishlist = Wishlist.objects.filter(profile=user_profile)
    wishlist_items = WishListItem.objects.all()
    users_wishlist_items = wishlist_items.filter(wishlist=users_wishlist[0])
    product_in_wishlist = users_wishlist_items.filter(product=product)

    product_in_wishlist.delete()
    messages.success(request,
                     'Product successfully removed from your wishlist.')

    return redirect(reverse('products'))


def remove_from_return_to_wishlist(request, product_id):
    ''' deletes wishlistitem and returns to wishlist view '''

    # gets wishlist item with users profile and product id
    product = Product.objects.get(pk=product_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    users_wishlist = Wishlist.objects.filter(profile=user_profile)
    wishlist_items = WishListItem.objects.all()
    users_wishlist_items = wishlist_items.filter(wishlist=users_wishlist[0])
    product_in_wishlist = users_wishlist_items.filter(product=product)

    product_in_wishlist.delete()
    messages.success(request,
                     'Product successfully removed from your wishlist.')

    return redirect(reverse('wishlist'))
