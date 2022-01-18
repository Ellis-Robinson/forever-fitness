from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Wishlist, WishListItem


class WishListItemAdminInline(admin.TabularInline):
    ''' adds wishlist item to wishlist admin sections '''
    model = WishListItem


class WishlistAdmin(admin.ModelAdmin):
    '''
    configurs Wishlist models admin display
    '''

    inlines = (WishListItemAdminInline,)

    formfield_overrides = {
        models.ManyToManyField: {
            'widget': CheckboxSelectMultiple
        },
    }


admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(WishListItem)
