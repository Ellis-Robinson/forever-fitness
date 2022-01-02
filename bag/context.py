from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    if total < settings.FREE_DELIVERY_FRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY_FRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'free_delivery_freshold': settings.FREE_DELIVERY_FRESHOLD,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total,
    }
    
    return context
