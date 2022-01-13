''' Classes and methods for workouts app '''
from django.db import models
from django.contrib.auth.models import User


class Workout(models.Model):
    '''
    A workout routine model, detailing key information for each routine
    '''

    title = models.CharField(max_length=250)
    type_of_workout = models.CharField(max_length=250)
    description = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return str(self.title)


class User_workouts(models.Model):
    '''
    A model connecting workouts to user profiles
    '''

    class Meta:
        ''' defines field name in admin '''
        verbose_name_plural = "User Workouts"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE,
                                related_name='workouts')