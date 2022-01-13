''' fitness classes models, admin registration '''
from django.contrib import admin
from .models import TypeOfFitness, FitnessClass


admin.site.register(FitnessClass)
admin.site.register(TypeOfFitness)
