from django import forms
from .models import Application

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

    class Meta:
        model = Application
        fields = ['school', 'grad_year', 'pronouns', 'race', 'hackathons', 'essay1', 'essay2', 'essay3', 'essay4', 'essay5', 'proudof', 'reimbursement', 'location']
        widgets = {
            'race': forms.CheckboxSelectMultiple(
                choices=RACE
            )
        }
