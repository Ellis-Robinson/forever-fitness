''' Classes and methods for workouts app '''
import datetime

from django.db import models
from django.utils.timezone import now
from django.core.validators import RegexValidator
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
                                        null=True, blank=True,
                                        on_delete=models.SET_NULL)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=250)
    duration = models.CharField(
        max_length=3, validators=[RegexValidator(
            regex='^[0-9]*$',
            message='Input must be numeric',)])
    users = models.ManyToManyField(UserProfile, blank=True)

    def __str__(self):
        return str(self.title)
