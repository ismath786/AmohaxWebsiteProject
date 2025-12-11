# callback/forms.py

from django import forms
from .models import CallbackRequest

class CallbackRequestForm(forms.ModelForm):
    class Meta:
        model = CallbackRequest
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Phone Number'}),
        }
