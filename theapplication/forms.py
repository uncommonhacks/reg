from django import forms
from .models import Application, Confirmation


class ApplicationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    resume = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["legal1"].widget.template_name="django/forms/widgets/legal1.html"
        self.fields["legal2"].widget.template_name="django/forms/widgets/legal2.html"

    class Meta:
        model = Application
        fields = "__all__"


class ConfirmationForm(forms.ModelForm):
    class Meta:
        model = Confirmation
        fields = "__all__"
