from django import forms
from .models import Application, Confirmation

RACE = (('W', 'White'),
        ('B', 'Black or African American'),
        ('N', 'American Indian or Alaska Native'),
        ('A', 'Asian'),
        ('P', 'Native Hawaiian or Pacific Islander'),
        ('H', 'Hispanic or Latino'))

class ApplicationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    
    class Meta:
        model = Application
        fields = '__all__'

class ConfirmationForm(forms.ModelForm):
    class Meta:
        model = Confirmation
        fields = '__all__'
