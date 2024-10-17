from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        mode=Profile
        fields='__all__'