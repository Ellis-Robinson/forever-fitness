''' Classes and methods for fitness_classes app '''
from django.db import models


class TypeOfFitness(models.Model):
    '''
    Defines type of fitness, used for fitness classes
    '''

    class Meta:
        ''' defines field name in admin '''
        verbose_name_plural = "Types of fitness"

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        ''' returns user friendly name '''
        return self.friendly_name


class FitnessClass(models.Model):
    '''
    A fitness class model, detailing key information for fitness classes
    '''

    class Meta:
        ''' defines field name in admin '''
        verbose_name_plural = "Fitness Classes"

    title = models.CharField(max_length=250)
    type_of_fitness = models.ForeignKey('TypeOfFitness', null=True,
                                        blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return str(self.title)
