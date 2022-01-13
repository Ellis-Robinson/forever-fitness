from django.urls import path
from . import views

urlpatterns = [
    path('', views.members_area, name='members_area'),
    path('my_workouts/', views.my_workouts, name='my_workouts')
]
