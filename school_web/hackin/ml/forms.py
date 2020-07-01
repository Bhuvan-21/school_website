from django import forms
from .models import mod

class mlform(forms.ModelForm):

        class Meta:
            model=mod
            fields='__all__'
