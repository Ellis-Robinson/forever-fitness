''' Classes and methods for workouts app '''
from django.db import models
from profiles.models import UserProfile
from django.utils.timezone import now

import datetime

class Workout(models.Model):
    '''
    A workout routine model, detailing key information for each routine
    '''

    title = models.CharField(max_length=250)
    type_of_workout = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField()
    date = models.DateField(default=(now() + datetime.timedelta(days=1)))
    location = models.CharField(max_length=250, default="online")
    duration = models.DurationField()
    users = models.ManyToManyField(UserProfile, null=True, blank=True)

    def __str__(self):
        return str(self.title)
