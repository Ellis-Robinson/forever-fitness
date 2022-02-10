''' holds form classes for workouts app '''
from django import forms
from .models import Workout, TypeOfWorkout


class DateInput(forms.DateInput):
    input_type = 'date'


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
        fields = ['title', 'type', 'description',
                  'date', 'location', 'duration']
        widgets = {
            'date': DateInput()
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        types_of_workout = TypeOfWorkout.objects.all()
        types = [(t.id, t.__str__()) for t in types_of_workout]

        placeholders = {
            'title': 'Workout Title',
            'type': 'Type',
            'description': 'Description',
            'date': 'Date',
            'location': 'Location',
            'duration': 'Duration in Minutes'
        }

        self.fields['type'].choices = types
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
