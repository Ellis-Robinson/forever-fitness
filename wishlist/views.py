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
    allows users to add product to their wishlist
    '''

    user_profile = get_object_or_404(UserProfile, user=request.user)
    users_wishlist = Wishlist.objects.filter(profile=user_profile)
    product = Product.objects.get(pk=product_id)

    new_item = WishListItem(wishlist=users_wishlist[0], product=product)
    new_item.save()

    messages.success(request, 'Product successfully added to your wishlist.')

    return redirect(reverse('products'))
