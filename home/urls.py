''' holds url patterns for home related views '''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]
