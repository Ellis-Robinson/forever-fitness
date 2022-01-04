from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


def update_on_save(sender, instance, created, **kwargs):
    '''
    update total on line item on create or update
    '''
    instance.order.update_total


def update_on_delete(sender, instance, **kwargs):
    '''
    update total on line item on delete
    '''
    instance.order.update_total