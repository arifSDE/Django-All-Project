from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        mode=Category
        fields='__all__'