''' Classes and methods for workouts app '''
from django.db import models


class TypeOfWorkout(models.Model):
    '''
    Defines type of workouts, used for fitness workouts
    '''

    class Meta:
        ''' defines field name in admin '''
        verbose_name_plural = "Types of workout"

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        ''' returns user friendly name '''
        return self.friendly_name


class WorkoutRoutine(models.Model):
    '''
    A workout routine model, detailing key information for each routine
    '''

    class Meta:
        ''' defines field name in admin '''
        verbose_name_plural = "Workout routines"

    title = models.CharField(max_length=250)
    type_of_workout = models.ForeignKey('TypeOfWorkout', null=True,
                                        blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return str(self.title)
