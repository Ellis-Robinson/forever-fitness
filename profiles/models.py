''' stores classes relating to profiles '''
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    '''
    a user profile model. Stores default delivery information and order history
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=11,
                                            null=True, blank=True,
                                            validators=[RegexValidator(
                                                regex='^[0-9]*$',
                                                message='Input must '
                                                'be numeric',)])
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_county = models.CharField(max_length=80,
                                      null=True, blank=True)
    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)
    default_country = CountryField(blank_label="Country",
                                   null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    '''
    create or update users profile
    '''
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
