''' defines wishlist class and related methods '''
from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    '''
    saves products to a specific profile
    '''
    name = models.CharField(default="My Wishlist",
                            max_length=250, null=True, blank=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class WishListItem(models.Model):

    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, related_name='wishitems')

    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)

    def __str__(self):
        return str(self.wishlist.profile)
