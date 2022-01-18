''' stores all functions for wishlist app '''
from django.shortcuts import render


def wishlist(request):
    ''' loads wishlist page '''

    return render(request, 'wishlist/wishlist.html')
