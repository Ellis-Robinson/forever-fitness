''' holds url patterns for workout related views '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.members_area, name='members_area'),
    path('my_workouts/', views.my_workouts, name='my_workouts'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('edit_workout/<int:workout_id>/', views.edit_workout,
         name='edit_workout'),
    path('delete_workout/<int:workout_id>/', views.delete_workout,
         name='delete_workout'),
    path('add_to_my_workouts/<workout_id>/', views.add_to_my_workouts,
         name='add_to_my_workouts'),
    path('remove_from_my_workouts/<workout_id>/',
         views.remove_from_my_workouts,
         name='remove_from_my_workouts'),
]
