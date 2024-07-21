from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import CustomUser

# form model used for registering users

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False, help_text="Select the group")

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2", "group"]
