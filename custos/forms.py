from django import forms
from .models import Cost

class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = ['categoria', 'valor', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'})
        }
