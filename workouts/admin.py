''' fitness classes models, admin registration '''
from django.contrib import admin
from .models import WorkoutRoutine, TypeOfWorkout


admin.site.register(WorkoutRoutine)
admin.site.register(TypeOfWorkout)
