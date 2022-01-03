''' stores all functions for bag app '''
from django.shortcuts import render, redirect, reverse, HttpResponse


def bag(request):
    ''' loads shopping bag view '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    ''' allows user to add items to bag '''
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'sizes' in request.POST:
        size = request.POST['sizes']
    shopping_bag = request.session.get('bag', {})

    if size:
        if item_id in list(shopping_bag.keys()):
            if size in shopping_bag[item_id]['items_by_size'].keys():
                shopping_bag[item_id]['items_by_size'][size] += quantity
            else:
                shopping_bag[item_id]['items_by_size'][size] = quantity
        else:
            shopping_bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(shopping_bag.keys()):
            shopping_bag[item_id] += quantity
        else:
            shopping_bag[item_id] = quantity

    request.session['bag'] = shopping_bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    ''' adjusts the quantity of item in bag '''
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'sizes' in request.POST:
        size = request.POST['sizes']
    shopping_bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            shopping_bag[item_id]['items_by_size'][size] = quantity
        else:
            del shopping_bag[item_id]['items_by_size'][size]
            if not shopping_bag[item_id]['items_by_size']:
                shopping_bag.pop(item_id)
    else:
        if quantity > 0:
            shopping_bag[item_id] = quantity
        else:
            shopping_bag.pop(item_id)

    request.session['bag'] = shopping_bag

    return redirect(reverse('bag'))


def remove_from_bag(request, item_id):
    ''' removes the item from shopping bag '''
    try:
        size = None
        if 'sizes' in request.POST:
            size = request.POST['sizes']
        shopping_bag = request.session.get('bag', {})

        if size:
            del shopping_bag[item_id]['items_by_size'][size]
            if not shopping_bag[item_id]['items_by_size']:
                shopping_bag.pop(item_id)
        else:
            shopping_bag.pop(item_id)

        request.session['bag'] = shopping_bag

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
