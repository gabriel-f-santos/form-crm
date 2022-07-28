from django import forms
from .models import Crm

class CrmForm(forms.ModelForm):
    class Meta:
        model = Crm
        fields = ("__all__")