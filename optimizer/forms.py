from django import forms
from .models import FarmData

class FarmDataForm(forms.ModelForm):
    class Meta:
        model = FarmData
        fields = ['farmer_name', 'total_budget', 'crop_options', 'transport_costs', 'constraints']
        widgets = {
            'crop_options': forms.Textarea(attrs={'rows': 2}),
            'transport_costs': forms.Textarea(attrs={'rows': 4}),
            'constraints': forms.Textarea(attrs={'rows': 4}),
        }
