from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='profile'),
    path('', views.user_orders, name='user_orders')
]
