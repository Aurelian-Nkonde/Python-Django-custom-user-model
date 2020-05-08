from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('age','city',)


class CustomChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('age','city',)