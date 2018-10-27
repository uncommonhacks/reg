from django.contrib import admin

from .models import Application, Confirmation, Applicant
 
# Register your models here.
#admin.site.register(RaceSelectMultiple)
admin.site.register(Application)
admin.site.register(Confirmation)
admin.site.register(Applicant)
    
