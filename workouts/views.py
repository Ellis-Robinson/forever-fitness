''' stores all functions for fitness_classes app '''
from django.shortcuts import render
from .models import WorkoutRoutine


def members_area(request):
    ''' loads fitness classes page '''

    routines = WorkoutRoutine.objects.all()

    template = 'workouts/members_area.html'
    context = {
        'routines': routines
    }

    return render(request, template, context)
