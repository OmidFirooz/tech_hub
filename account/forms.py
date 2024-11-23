from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model: Profile
        field = ['bio', 'profile_picture', 'github_link']