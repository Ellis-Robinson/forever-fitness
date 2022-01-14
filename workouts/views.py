''' stores all functions for fitness_classes app '''
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from .models import Workout
from .forms import WorkoutForm


def members_area(request):
    ''' loads fitness classes page '''

    workouts = Workout.objects.all()

    template = 'workouts/members_area.html'
    context = {
        'workouts': workouts
    }

    return render(request, template, context)

@login_required
def my_workouts(request):
    ''' loads page with users saved classes '''
    users_profile = get_object_or_404(UserProfile, user=request.user)
    workouts = Workout.objects.filter(users=users_profile)

    template = 'workouts/my_workouts.html'
    context = {
        'workouts': workouts
    }

    return render(request, template, context)


@login_required
def add_workout(request):
    '''
    allows superusers to add fitness classes to database
    '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = WorkoutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workout successfully added.')
            return redirect(reverse('members_area'))
        else:
            messages.error(request,
                           'Failed to add workout. Is the form valid?')
    else:
        form = WorkoutForm()

    template = 'workouts/add_workout.html'
    context = {
        'form': form
    }
    return render(request, template, context)


@login_required
def edit_workout(request, workout_id):
    ''' update a workout in database '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    workout = get_object_or_404(Workout, pk=workout_id)
    if request.method == "POST":
        form = WorkoutForm(request.POST, request.FILES, instance=workout)
        if form.is_valid():
            form.save()
            messages.success(request, 'Workout successfully updated.')
            return redirect(reverse('members_area'))
        else:
            messages.error(request,
                           f'Failed to update {workout.title}.'
                           'Is the form valid?')
    else:
        form = WorkoutForm(instance=workout)
        messages.info(request, f'you are editing {workout.title}')

    template = 'workouts/edit_workout.html'
    context = {
        'form': form,
        'workout': workout,
    }

    return render(request, template, context)


@login_required
def delete_workout(request, workout_id):
    ''' Delete a workout from database '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    workout = get_object_or_404(Workout, pk=workout_id)

    if request.method == "POST":

        workout.delete()
        messages.success(request, f'{workout.title} deleted')

        return redirect(reverse('members_area'))

    else:
        template = 'workouts/delete_workout.html'
        context = {
            'workout': workout,
        }
        return render(request, template, context)
