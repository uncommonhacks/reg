from django import forms
from .models import Application, Confirmation


class ApplicationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    resume = forms.FileField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["legal1"].widget.template_name = "django/forms/widgets/legal1.html"
        self.fields["legal2"].widget.template_name = "django/forms/widgets/legal2.html"
        self.fields["legal3"].widget.template_name = "django/forms/widgets/legal3.html"
        self.fields["brain_1"].widget.template_name = "django/forms/widgets/brain1.html"
        self.fields["is_this_a"].widget.template_name = "django/forms/widgets/isthisa.html"
        self.fields["pikachu"].widget.template_name = "django/forms/widgets/pikachu.html"

    class Meta:
        model = Application
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "birth_date",
            "gender",
            "pronouns",
            "race",
            "school",
            "major",
            "study_level",
            "grad_year",
            "location",
            "hackathons",
            "self_description",
            "proudof",
            "essay1",
            "essay2",
            "essay3",
            "brain_1",
            "brain_2",
            "brain_3",
            "brain_4",
            "is_this_a",
            "pikachu",
            "resume",
            "legal1",
            "legal2",
            "legal3",
        ]


class ConfirmationForm(forms.ModelForm):
    class Meta:
        model = Confirmation
        fields = "__all__"
