''' fitness classes models, admin registration '''
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Workout, TypeOfWorkout


class WorkoutAdmin(admin.ModelAdmin):
    '''
    configurs Workout models admin display
    '''
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': CheckboxSelectMultiple
        },
    }


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(TypeOfWorkout)
