"""
Forms
"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    CustomUserCreationForm
    """
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('name',)


class CustomUserChangeForm(UserChangeForm):
    """
    CustomUserChangeForm
    """
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
