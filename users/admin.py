from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomChange, CustomCreation
from .models import CustomUser

class CustomAdmin(UserAdmin):
    add_form = CustomCreation
    form = CustomChange
    model = CustomUser
    list_display = ['username','is_staff','is_active','age','city']

admin.site.register(CustomUser, CustomAdmin)