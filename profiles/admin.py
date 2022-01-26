''' registers profile models for use in admin section '''
from django.contrib import admin
from .models import UserProfile


admin.site.register(UserProfile)
