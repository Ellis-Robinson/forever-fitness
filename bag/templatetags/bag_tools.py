''' stores custom template tags'''
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    ''' calculates subtotal based on quantity '''

    return price * quantity
