''' stores all functions for bag app '''
from django.shortcuts import render, redirect


def bag(request):
    ''' loads shopping bag view '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    ''' allows user to add items to bag '''
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('bag', {})
    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity
    request.session['bag'] = shopping_bag
    return redirect(redirect_url)
