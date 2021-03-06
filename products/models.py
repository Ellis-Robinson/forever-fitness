''' stores all classes relating to products '''

from django.db import models


class Category (models.Model):
    '''
    defines fields for Category class
    '''
    class Meta:
        ''' defines field name in admin '''
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        ''' returns user friendly name '''
        return self.friendly_name


class Product(models.Model):
    '''
    defines fields for Products class
    '''
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
