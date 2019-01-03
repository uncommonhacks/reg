from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from registration.backends.default.views import ActivationView
from . import models
from . import forms
from django.http import HttpResponse
from .settings import over_application_deadline, over_confirmation_deadline, con_deadline_dt
from .storage_backends import upload_resume_to_s3
from django.db.models import Q

# Create your views here.


class ApplicantActivationView(ActivationView):
    def activate(self, *args, **kwargs):
        user = super(ApplicantActivationView, self).activate(*args, **kwargs)
        applic = models.Applicant(
            user=user,
            application=None,
            confirmation=None,
            notified_of_admit_status=False,
            status="NS",
        )
        applic.save()
        return user

def stats_page(request):
    total_applicants = models.Applicant.objects.count()
    total_applied = models.Application.objects.count()
    total_confirmed = models.Confirmation.objects.count()

    number_without_decision = models.Applicant.objects.filter(status='AD').count()
    number_waitlisted = models.Applicant.objects.filter(status='WA').count()
    number_not_admitted = models.Applicant.objects.filter(status='NA').count()
    number_admitted = models.Applicant.objects.filter(status='AM').count()
    total_admits_confirms = number_admitted + total_confirmed

    admitted_queryset = models.Applicant.objects.filter(Q(status='AM') | Q(status='CF')).all()

    admitted_apps = [a.application for a in admitted_queryset]

    count_by_gender = lambda g: len([a for a in admitted_apps if a.gender == g])

    admitted_gender_stats = {gender[1]: count_by_gender(gender[0])/admitted_queryset.count()
            for gender in models.Application.GENDER_CHOICES}

    count_by_class_year = lambda cy: len([a for a in admitted_apps if a.study_level == cy])

    class_year_stats = {class_year[1]: count_by_class_year(class_year[0])/admitted_queryset.count()
            for class_year in models.Application.STUDY_LEVEL_CHOICES}

    STATS_DICT = [
            ('total users in system', total_applicants),
            ('total applications submitted', total_applied),
            ('number of confirmations', total_confirmed),
            ('applications without decisions', number_without_decision),
            ('number waitlisted', number_waitlisted),
            ('number not admitted', number_not_admitted),
            ('number admitted but not confirmed', number_admitted),
            ('number admitted and confirmed', total_admits_confirms),
            ('gender stats of admitted applicants', admitted_gender_stats),
            ('class year stats of admitted applicants', class_year_stats),
            ]
    return render(request, 'in_app/reviewer_index.html', context={'stats': STATS_DICT})

@login_required
def index(request):
    if not models.Applicant.objects.filter(user=request.user).exists():
        return stats_page(request)
    applicant_obj = models.Applicant.objects.get(user=request.user)
    status = applicant_obj.get_status_display()
    open_application = applicant_obj.status == "NS" and not over_application_deadline()
    open_confirmation = applicant_obj.status == "AM" and not over_confirmation_deadline()
    over_app_deadline = applicant_obj.status == "NS" and over_application_deadline()
    over_conf_deadline = applicant_obj.status == "AM" and over_confirmation_deadline()
    conf_deadline = con_deadline_dt
    return render(
        request,
        "in_app/applicant_index.html",
        context={
            "status": status,
            "open_application": open_application,
            "open_confirmation": open_confirmation,
            "over_application_deadline": over_app_deadline,
            "over_confirmation_deadline": over_conf_deadline,
            "conf_deadline": con_deadline_dt
        },
    )

@login_required
def application(request):
    if not models.Applicant.objects.filter(user=request.user).exists():
        return redirect("/")
    applicant = models.Applicant.objects.get(user=request.user)
    if applicant.status != "NS" or over_application_deadline():
        return redirect("/")
    if request.method == "POST":
        form = forms.ApplicationForm(request.POST, request.FILES)
        if not form.is_valid():
            pass
        elif not upload_resume_to_s3(request.FILES["resume"], request.user):
            form.add_error("resume", "Resume should be a PDF smaller than 10MB!")
        else:
            user = request.user
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.save()
            application = form.save()
            applicant.application = application
            applicant.status = "AD"
            applicant.save()
            return redirect("/")
    else:
        form = forms.ApplicationForm()
    return render(
        request,
        "in_app/application.html",
        {"form": form, "enctype": "enctype=multipart/form-data"},
    )


@login_required
def confirmation(request):
    if not models.Applicant.objects.filter(user=request.user).exists():
        return redirect("/")
    applicant = models.Applicant.objects.get(user=request.user)
    if applicant.status != "AM" or over_confirmation_deadline():
        return redirect("/")
    if request.method == "POST":
        form = forms.ConfirmationForm(request.POST)
        if form.is_valid():
            confirmation = form.save()
            applicant.confirmation = confirmation
            applicant.status = "CF"
            applicant.save()
            return redirect("/")
    else:
        form = forms.ConfirmationForm()
    return render(
        request, 
        "in_app/confirmation.html", 
        {"form": form, "enctype": ""},
    )
