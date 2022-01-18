''' stores all functions for wishlist app '''
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from profiles.models import UserProfile
from products.models import Product

from .models import Wishlist, WishListItem


def wishlist(request):
    ''' loads wishlist page '''

    user_profile = get_object_or_404(UserProfile, user=request.user)
    users_wishlist = Wishlist.objects.filter(profile=user_profile)
    items = WishListItem.objects.all()
    users_items = items.filter(wishlist=users_wishlist[0])

    template = 'wishlist/wishlist.html'
    context = {
        'template': template,
        'wishlist': users_wishlist,
        'items': users_items
    }

    return render(request, template, context)


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


def remove_from_wishlist(request, product_id):
    ''' deletes wishlistitem '''

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
