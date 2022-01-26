'''
views and functions for profile app
'''
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from wishlist.models import Wishlist
from checkout.models import Order

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def user_profile(request):
    ''' renders users profile '''
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile successfully updated")
        else:
            messages.error(request, 'Unable to update profile.'
                           ' Is the form valid?')

    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    # creates list of user profiles with wishlists attached
    wishlists = Wishlist.objects.all()
    wishlist_users = []
    for wishlist in wishlists:
        wishlist_users.append(wishlist.profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'user': profile,
        'wishlists': wishlist_users
    }

    return render(request, template, context)


@login_required
def user_orders(request):
    ''' renders users orders page'''
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/user_orders.html'
    context = {
        'orders': orders.order_by('-date'),
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    ''' renders template for user to view past orders '''
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
