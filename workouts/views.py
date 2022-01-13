''' stores all functions for fitness_classes app '''
from django.shortcuts import render, get_object_or_404
from .models import Workout, User_workouts


def members_area(request):
    ''' loads fitness classes page '''

    workouts = Workout.objects.all()

    template = 'workouts/members_area.html'
    context = {
        'workouts': workouts
    }

    return render(request, template, context)


def my_workouts(request):
    ''' loads page with users saved routines '''

    workouts = get_object_or_404(User_workouts, user=request.user)

    template = 'workouts/my_workouts.html'
    context = {
        'workouts': workouts
    }

    return render(request, template, context)
