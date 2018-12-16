from django.db import models
from django.contrib.auth.models import User

class RaceChoice(models.Model):
    
    race_string = models.CharField(max_length=50)

    def __str__(self):
        return self.race_string
# application class, to attach to applicant class
class Application(models.Model):
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
    
    
    GENDER_CHOICE = (
        ('M_', 'Male'),
        ('NB', 'Nonbinary'),
        ('F_', 'Female'),
        ('or', 'Other/Prefer not to disclose'),
    )
    gender = models.CharField(
            max_length=2,
            choices=GENDER_CHOICES,
            default='or',
    )

    major = models.CharField(max_length=150)
    
    # race
    race = models.ManyToManyField(RaceChoice)

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

# confirmation class, to attach to applicant class
class Confirmation(models.Model):
    phone_number = models.CharField(max_length=20)
    
    dietary_restrictions = models.CharField(max_length=1000)
    
    SHIRT_SIZE_CHOICES = (
        ('XS', 'XS'),
        ('S_', 'S'),
        ('M_', 'M'),
        ('L_', 'L'),
        ('1X', 'XL'),
        ('2X', 'XXL'),
    )
    shirt_size = models.CharField(
            max_length=2,
            choices=SHIRT_SIZE_CHOICES,
            default='M_'
    )

    notes = models.TextField(max_length=1500)


class Applicant(models.Model):
    def __str__(self):
        return '{}: {} {}'.format(self.user.username, self.user.first_name, self.user.last_name)
    
    # user model, handles email/auth/name
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    
    # whats their app status?
    STATUS_CHOICES = (
        ('NS', 'Application Not Started'),
        ('AD', 'Awaiting Decision'),
        ('WA', 'Waitlist'),
        ('NA', 'Not Admitted'),
        ('AM', 'Admitted'),
        ('CF', 'Confirmed'),
    )
    status = models.CharField(
                max_length=2,
                choices=STATUS_CHOICES,
                default='NS'
            )

    notified_of_admit_status = models.BooleanField(default=False)
    # attach their application
    application = models.OneToOneField(Application, null=True, on_delete=models.SET_NULL, blank=True)
    
    confirmation = models.OneToOneField(Confirmation, null=True, on_delete=models.SET_NULL, blank=True)
