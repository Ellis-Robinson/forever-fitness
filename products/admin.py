'''
houses classes for organising how admin section is displayed
'''

from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    ''' set field display order and ordering in admin '''
    list_display = ('sku', 'name', 'category',
                    'price', 'rating', 'image',)
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    ''' set field display order in admin '''
    list_display = ('friendly_name', 'name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
