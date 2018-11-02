from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from registration.backends.default.views import ActivationView
from . import models
from . import forms
from django.http import HttpResponse

# Create your views here.

class ApplicantActivationView(ActivationView):
    def activate(self, *args, **kwargs):
        user = super(ApplicantActivationView, self).activate(*args, **kwargs)
        applic = models.Applicant(user=user, application=None, confirmation=None, status="NS")
        applic.save()
        return user

@login_required
def index(request):
    if models.Applicant.objects.filter(user=request.user).exists():
        applicant_obj = models.Applicant.objects.get(user=request.user)
        return render(request, 'in_app/applicant_index.html', context={'status': applicant_obj.get_status_display()})
    else:
        return render(request, 'in_app/reviewer_index.html')

@login_required
def application(request):
    if request.method == 'POST':
        # what to do if form is already filled out?
        form = forms.ApplicationForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = forms.ApplicationForm()
    return render(request, 'in_app/application.html', {'form':form.as_p})
        # make the application object and fill the field

        # attach it to the current user

        # change the user's status


