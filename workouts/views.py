''' stores all functions for fitness_classes app '''
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Workout
from profiles.models import UserProfile
from .forms import WorkoutForm


def members_area(request):
    ''' loads fitness classes page '''

    workouts = Workout.objects.all()

    template = 'workouts/members_area.html'
    context = {
        'workouts': workouts
    }

    return render(request, template, context)


def my_workouts(request):
    ''' loads page with users saved classes '''

    users_profile = get_object_or_404(UserProfile, user=request.user)
    workouts = Workout.objects.filter(users=users_profile)

    template = 'workouts/my_workouts.html'
    context = {
        'workouts': workouts
    }

    return render(request, template, context)


def add_workout(request):
    '''
    allows superusers to add fitness classes to database
    '''

    form = WorkoutForm()

    template = 'workouts/add_workout.html'
    context = {
        'form': form
    }
    return render(request, template, context)
