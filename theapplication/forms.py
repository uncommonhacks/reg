from django import forms
from .models import Application, Confirmation

RACE = (('W', 'White'),
        ('B', 'Black or African American'),
        ('N', 'American Indian or Alaska Native'),
        ('A', 'Asian'),
        ('P', 'Native Hawaiian or Pacific Islander'),
        ('H', 'Hispanic or Latino'))

class ApplicationForm(forms.ModelForm):
    is_adult = forms.BooleanField()
    inforelease = forms.BooleanField()
    terms_conditions = forms.BooleanField()
    code_of_conduct = forms.BooleanField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Application
        fields = ['school', 'grad_year', 'pronouns', 'gender', 'race', 'major', 'hackathons', 'essay1', 'essay2', 'essay3', 'essay4', 'essay5', 'proudof', 'reimbursement', 'location']

class ConfirmationForm(forms.ModelForm):
    class Meta:
        model = Confirmation
        fields = ['phone_number', 'dietary_restrictions', 'shirt_size', 'notes']
