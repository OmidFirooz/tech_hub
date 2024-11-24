from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model: Profile
        field = ['bio', 'profile_picture', 'github_link']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }