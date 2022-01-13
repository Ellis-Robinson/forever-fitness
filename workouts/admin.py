''' fitness classes models, admin registration '''
from django.contrib import admin
from .models import Workout, User_workouts


admin.site.register(Workout)
admin.site.register(User_workouts)
