from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        mode=Author
        fields='__all__'