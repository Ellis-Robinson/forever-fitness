''' fitness classes models, admin registration '''
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Workout


class WorkoutAdmin(admin.ModelAdmin):
    '''
    sorts out workouts admin
    '''
    formfield_overrides = {
        models.ManyToManyField: {
            'widget': CheckboxSelectMultiple
        },
    }


admin.site.register(Workout, WorkoutAdmin)
