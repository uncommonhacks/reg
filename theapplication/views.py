from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from registration.backends.default.views import ActivationView
from . import models
from . import forms
from django.http import HttpResponse
from .settings import over_application_deadline, over_confirmation_deadline

# Create your views here.

class ApplicantActivationView(ActivationView):
    def activate(self, *args, **kwargs):
        user = super(ApplicantActivationView, self).activate(*args, **kwargs)
        applic = models.Applicant(user=user, application=None, confirmation=None, notified_of_admit_status=False, status="NS")
        applic.save()
        return user

@login_required
def index(request):
    applicant_obj = models.Applicant.objects.get(user=request.user)
    status = applicant_obj.get_status_display()
    open_application = applicant_obj.status == 'NS' and not over_application_deadline()
    open_confirmation = applicant_obj.status == 'AM' and not over_confirmation_deadline()
    over_app_deadline = applicant_obj.status == 'NS' and over_application_deadline()
    over_conf_deadline = applicant_obj.status == 'AM' and over_confirmation_deadline()
    return render(request, 'in_app/applicant_index.html', context={'status': status, 'open_application': open_application, 'open_confirmation': open_confirmation, 'over_application_deadline': over_app_deadline, 'over_confirmation_deadline': over_conf_deadline})

@login_required
def application(request):
    if not models.Applicant.objects.filter(user=request.user).exists():
        return redirect('/')
    applicant = models.Applicant.objects.get(user=request.user)
    if applicant.status != 'NS' or over_application_deadline():
        return redirect('/')
    if request.method == 'POST':
        form = forms.ApplicationForm(request.POST)
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            application = form.save()
            applicant.application = application
            applicant.status = 'AD'
            applicant.save()
            return redirect('/')
    else:
        form = forms.ApplicationForm()
    return render(request, 'in_app/application.html', {'form':form.as_p})

@login_required
def confirmation(request):
    if not models.Applicant.objects.filter(user=request.user).exists():
        return redirect('/')
    applicant = models.Applicant.objects.get(user=request.user)
    if applicant.status != 'AM' or over_confirmation_deadline():
        return redirect('/')
    if request.method == 'POST':
        form = forms.ConfirmationForm(request.POST)
        if form.is_valid:
            confirmation = form.save()
            applicant.confirmation = confirmation
            applicant.status = 'CF'
            applicant.save()
            return redirect('/')
    else:
        form = forms.ConfirmationForm(request.POST)
    return render(request, 'in_app/confirmation.html', {'form': form.as_p})
