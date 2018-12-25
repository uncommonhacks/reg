from django.contrib import admin

from .models import RaceChoice, Application, Confirmation, Applicant

# Register your models here.
admin.site.register(RaceChoice)
admin.site.register(Application)
admin.site.register(Confirmation)
admin.site.register(Applicant)
