from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from registration.backends.default.views import ActivationView
from . import models

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
