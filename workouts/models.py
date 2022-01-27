''' Classes and methods for workouts app '''
import datetime

from django.db import models
from django.utils.timezone import now
from profiles.models import UserProfile


class TypeOfWorkout(models.Model):
    '''
    a type of workout used in Workout model
    '''

    name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Workout(models.Model):
    '''
    A workout routine model, detailing key information for each routine
    '''

    title = models.CharField(max_length=250)
    type_of_workout = models.ForeignKey(TypeOfWorkout,
                                        on_delete=models.SET_NULL,
                                        null=True, blank=True)
    description = models.TextField()
    date = models.DateField(default=(now() + datetime.timedelta(days=1)))
    location = models.CharField(max_length=250, default="online")
    duration = models.CharField(max_length=250)
    users = models.ManyToManyField(UserProfile, blank=True)

    def __str__(self):
        return str(self.title)
