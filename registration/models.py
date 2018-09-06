from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Applicant(models.Model):
    # user model, handles email/auth/name
    user = models.OneToOneField(User)
    
    # whats their app status?
    # TODO set up an enum for this
    status = models.CharField(max_length=200)
    
    # attach their application
    application = models.OneToOneField(Application, null=True)


    
class Application(models.Model):
    # are they 18+
    is_adult = models.BooleanField(default=False)
    
    # what's their school
    # TODO: make this a selector not a text field
    school = models.CharField(max_length=200)

    # what's graduation year?
    # Constants in Model class
    YEAR_IN_SCHOOL_CHOICES = (
        ('19', '2019'),
        ('20', '2020'),
        ('21', '2021'),
        ('22', '2022'),
        ('23', '2023 or Later'),
        ('or', 'other'),
    )
    grad_year = models.CharField(
            max_length=2,
            choices=YEAR_IN_SCHOOL_CHOICES,
            default='or'
    )
    
    # pronouns text field
    pronouns = models.CharField(max_length=150)

    # race TODO make this a multi-selector
    race = models.CharField(max_length=150)

    # prior hackathons TODO make this a selector
    hackathons = models.CharField(max_length=150)
    
    # essay questions
    essay1 = models.TextField(max_length=1500)
    essay2 = models.TextField(max_length=1500)
    essay3 = models.TextField(max_length=1500)
    essay4 = models.TextField(max_length=1500)
    essay5 = models.TextField(max_length=1500)

    # show us something you're proud of
    proudof = models.TextField(max_length=1500)

    # do they need reimbursement
    reimbursement = models.BooleanField(default=False)

    # where are they coming from?
    location = models.CharField(max_length=200)

    inforelease = models.BooleanField(default=False)
    termsconditions = models.BooleanField(default=False)
    code_of_conduct = models.BooleanField(default=False)
