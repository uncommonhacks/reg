from django import forms
from .models import Application, Confirmation


class ApplicationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    resume = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Constrain race options
        self.fields['race'] = forms.MultipleChoiceField(choices=RACE_CHOICES,)
        # Make school an autocomplete field
#        self.fields['school'].widget.template_name=("django/forms/widgets/"
#                                                    "school_autocomplete.html")

    class Meta:
        model = Application
        fields = '__all__'

class ConfirmationForm(forms.ModelForm):
    class Meta:
        model = Confirmation
        fields = '__all__'
