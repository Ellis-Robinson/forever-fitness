''' stores all functions for fitness_classes app '''
from django.shortcuts import render
from .models import FitnessClass


def members_area(request):
    ''' loads fitness classes page '''

    classes = FitnessClass.objects.all() 

    template = 'fitness_classes/members_area.html'
    context = {
        'classes': classes
    }

    return render(request, template, context)
