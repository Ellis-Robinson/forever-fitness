''' stores all functions for bag app '''
from django.shortcuts import render


def bag(request):
    ''' loads shopping bag view '''

    return render(request, 'bag/bag.html')
