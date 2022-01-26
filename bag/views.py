''' stores all functions for bag app '''
from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def bag(request):
    ''' loads shopping bag view '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    ''' allows user to add items to bag '''
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'size' in request.POST:
        size = request.POST['size']
    shopping_bag = request.session.get('bag', {})

    # checks if item has a size
    if size:
        # checks if item already in bag
        if item_id in list(shopping_bag.keys()):
            # checks if that item of that size already in bag
            if size in shopping_bag[item_id]['items_by_size'].keys():
                # updates quantity of item of that size
                shopping_bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, (
                        f'Updated size {size.upper()} {product.name}'
                        'quantity to'
                        f'{shopping_bag[item_id]["items_by_size"][size]}'))
            else:
                # adds item of that size to bag
                shopping_bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, 'Added size'
                                 f'{size.upper()} {product.name} to your bag')
        else:
            # adds item of that size to bag
            shopping_bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, 'Added size'
                             f'{size.upper()} {product.name} to your bag')
    else:
        # checks if item already in bag
        if item_id in list(shopping_bag.keys()):
            # increases quantity of item in bag
            shopping_bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name}'
                f'quantity to {shopping_bag[item_id]}')
        else:
            # adds item to bag
            shopping_bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag.')

    request.session['bag'] = shopping_bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    '''
    adjusts the quantity of item in bag
    or removes it if quantity set to 0
    '''
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_bag = request.session.get('bag', {})

    # checks if item has size
    if size:
        if quantity > 0:
            # updates item with new quantity
            shopping_bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             f'Updated size {size.upper()} {product.name}'
                             ' quantity to '
                             f'{shopping_bag[item_id]["items_by_size"][size]}')
        else:
            # removes item from bag
            del shopping_bag[item_id]['items_by_size'][size]
            if not shopping_bag[item_id]['items_by_size']:
                shopping_bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()}'
                             f'{product.name} from your bag')
    else:
        # updates item with new quantity
        if quantity > 0:
            shopping_bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to'
                             f'{shopping_bag[item_id]}')
        else:
            # removes item from bag
            shopping_bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = shopping_bag

    return redirect(reverse('bag'))


def remove_from_bag(request, item_id):
    ''' removes the item from shopping bag '''
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        shopping_bag = request.session.get('bag', {})

        # checks if item has size
        if size:
            # removes item from bag
            del shopping_bag[item_id]['items_by_size'][size]
            if not shopping_bag[item_id]['items_by_size']:
                shopping_bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()}'
                             f'{product.name} from your bag')
        else:
            # removes item from bag
            shopping_bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = shopping_bag

        return HttpResponse(status=200)

    except Exception as error:
        messages.error(request, f'Error removing item: {error}')
        return HttpResponse(status=500)
