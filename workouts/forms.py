''' holds form classes for workouts app '''
from django import forms
from .models import Workout


class WorkoutForm(forms.ModelForm):
    '''
    A form for super users to add workouts
    '''
    class Meta:
        '''
        defines which class is connected to the form
        and which fields from that class to generate
        '''
        model = Workout
        exclude = ['users']
