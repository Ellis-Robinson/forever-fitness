''' stores all functions for fitness_classes app '''
from datetime import date
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from .models import Workout, TypeOfWorkout
from .forms import WorkoutForm


@login_required
def members_area(request):
    ''' loads fitness classes page '''

    workouts = Workout.objects.all()
    types_of_workout = TypeOfWorkout.objects.all()
    today = date.today()

    template = 'workouts/members_area.html'
    context = {
        'workouts': workouts,
        'today': today,
        'types_of_workout': types_of_workout
    }

    return render(request, template, context)


@login_required
def my_workouts(request):
    ''' loads page with users saved classes '''
    users_profile = get_object_or_404(UserProfile, user=request.user)
    workouts = Workout.objects.filter(users=users_profile)
    types_of_workout = TypeOfWorkout.objects.all()
    today = date.today()

    template = 'workouts/my_workouts.html'
    context = {
        'workouts': workouts,
        'today': today,
        'types_of_workout': types_of_workout
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
    types_of_workout = TypeOfWorkout.objects.all()

    if request.method == "POST":

        workout.delete()
        messages.success(request, f'{workout.title} deleted')

        return redirect(reverse('members_area'))

    else:
        template = 'workouts/delete_workout.html'
        context = {
            'workout': workout,
            'types_of_workout': types_of_workout
        }
        return render(request, template, context)


@login_required
def add_to_my_workouts(request, workout_id):
    '''
    Allows users to link their profile to workouts
    '''

    workout = get_object_or_404(Workout, pk=workout_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    today = date.today()

    if workout.date < today:
        messages.error(request, 'Sorry, that class has already happened,'
                       ' please choose another')
    elif profile in workout.users.all():
        messages.success(request, 'Workout already in your workouts!')
    else:
        workout.users.add(profile)
        messages.success(request,
                         'Workout succesfully added to your workouts!')

    return redirect(reverse('members_area'))


@login_required
def remove_from_my_workouts(request, workout_id):
    '''
    Allows users to link their profile to workouts
    '''

    workout = get_object_or_404(Workout, pk=workout_id)
    profile = get_object_or_404(UserProfile, user=request.user)

    workout.users.remove(profile)

    messages.success(request, 'Workout succesfully removed to your workouts')

    return redirect(reverse('my_workouts'))
