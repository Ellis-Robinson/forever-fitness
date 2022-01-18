''' stores all functions for wishlist app '''
from django.shortcuts import render, get_object_or_404
from .models import Wishlist, WishListItem
from profiles.models import UserProfile


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
