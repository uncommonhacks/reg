from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class RaceChoice(models.Model):
    race_string = models.CharField(max_length=50)

    def __str__(self):
        return self.race_string


class SchoolChoice(models.Model):
    school_string = models.CharField(max_length=200)

    def __str__(self):
        return self.school_string


# Application class, to attach to applicant class.
class Application(models.Model):

    phone_number = models.CharField(
        max_length=20, null=True, 
        verbose_name="Phone Number", 
        help_text="###-###-####"
    )

    birth_date = models.DateField(
        null=True,
        verbose_name="Birth Date",
        help_text=(
            "MM/DD/YYYY - Because of limitations imposed by "
            "our venue, we are not legally allowed to host "
            "minors (those under 18) for Uncommon Hacks 2019."
        ),
    )

    GENDER_CHOICES = (
        ("M_", "Male"),
        ("NB", "Nonbinary"),
        ("F_", "Female"),
        ("O_", "Other"),
        ("P_", "Prefer not to answer"),
    )

    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)

    pronouns = models.CharField(
        max_length=150, verbose_name="What are your pronouns?", null=True
    )

    race = models.ManyToManyField(
        RaceChoice, verbose_name="What is your race/ethnicity?"
    )

    school = models.ForeignKey(
        SchoolChoice,
        verbose_name=(
            "Where do you attend school?"
        ),
        help_text="If your school does not appear on the list, select \"Other\"",
        on_delete="SET_NULL",
        null=True,
    )

    major = models.CharField(
        max_length=150, verbose_name="What is your major?", null=True
    )
    STUDY_LEVEL_CHOICES = (
        ("HS", "High school or below"),
        ("1Y", "1st year"),
        ("2Y", "2nd year"),
        ("3Y", "3rd year"),
        ("4Y", "4th year"),
        ("5Y", "5th year and beyond"),
        ("GS", "Graduate Student"),
        ("GR", "Graduated/out of school"),
    )

    study_level = models.CharField(
        max_length=2,
        verbose_name="What is your current level of study?",
        choices=STUDY_LEVEL_CHOICES,
        null=True,
    )

    YEAR_IN_SCHOOL_CHOICES = (
        ("19", "2019"),
        ("20", "2020"),
        ("21", "2021"),
        ("22", "2022"),
        ("23", "2023 or later"),
        ("or", "Other"),
    )

    grad_year = models.CharField(
        max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, null=True
    )

    location = models.CharField(
        max_length=200,
        verbose_name="Where are you coming from to attend Uncommon Hacks?",
        help_text="city, province, country",
        null=True,
    )

    hackathons = models.CharField(
        max_length=150,
        verbose_name="Which hackathons, if any, have you attended before?",
        null=True,
    )

    self_description = models.CharField(
        max_length=1500, verbose_name="I would describe myself as...", null=True
    )

    proudof = models.TextField(
        max_length=1500,
        verbose_name="Anything you're proud of (Github, Devpost, etc.) ?",
        null=True,
    )

    essay1 = models.TextField(
        max_length=1500,
        verbose_name=(
            "There are 2 types of people in this world. "
            "One is you. The other is everyone else. "
            "What are the types?"
        ),
        null=True,
    )
    essay2 = models.TextField(
        max_length=1500,
        verbose_name=(
            "Sandwich (noun): A popular concoction consisting "
            "of two or more pieces of surrounding material "
            "with various other materials in between them. "
            "This definition leads to the very obvious "
            "question that I’m sure you’re already thinking "
            "of: is an array a sandwich?"
        ),
        null=True,
    )
    essay3 = models.TextField(
        max_length=1500,
        verbose_name=(
            "If you could create your own flavor of La Croix, "
            "what would it be and why? What would it be "
            "called? What would it taste like--to the degree "
            "that you can actually taste it ;) "
        ),
        null=True,
    )

    legal1 = models.BooleanField(default=False, verbose_name="")

    legal2 = models.BooleanField(default=False, verbose_name="")

    legal3 = models.BooleanField(default=False, verbose_name="")

    brain_1 = models.CharField(
        max_length=150, verbose_name="", null=True,
    )

    brain_2 = models.CharField(
        max_length=150, verbose_name="Expanding Brain 2", null=True
    )

    brain_3 = models.CharField(
        max_length=150, verbose_name="Expanding Brain 3", null=True
    )

    brain_4 = models.CharField(
        max_length=150, verbose_name="Expanding Brain 4", null=True
    )

    is_this_a_1 = models.CharField(max_length=150, verbose_name="Who", null=True)

    is_this_a_2 = models.CharField(max_length=150, verbose_name="Butterfly", null=True)

    is_this_a_3 = models.CharField(max_length=150, verbose_name="Is this...", null=True)

    pikachu = models.TextField(max_length=500, verbose_name="", null=True)


# confirmation class, to attach to applicant class
class Confirmation(models.Model):
    dietary_restrictions = models.CharField(max_length=1000)

    SHIRT_SIZE_CHOICES = (
        ("XS", "XS"),
        ("S_", "S"),
        ("M_", "M"),
        ("L_", "L"),
        ("1X", "XL"),
        ("2X", "XXL"),
    )
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZE_CHOICES, null=True)

    notes = models.TextField(max_length=1500)


class Applicant(models.Model):
    def __str__(self):
        return "{}: {} {}".format(
            self.user.username, self.user.first_name, self.user.last_name
        )

    # user model, handles email/auth/name
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)

    # whats their app status?
    STATUS_CHOICES = (
        ("NS", "Application Not Started"),
        ("AD", "Awaiting Decision"),
        ("WA", "Waitlist"),
        ("NA", "Not Admitted"),
        ("AM", "Admitted"),
        ("CF", "Confirmed"),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="NS")

    notified_of_admit_status = models.BooleanField(default=False)
    # attach their application
    application = models.OneToOneField(
        Application, null=True, on_delete=models.SET_NULL, blank=True
    )

    confirmation = models.OneToOneField(
        Confirmation, null=True, on_delete=models.SET_NULL, blank=True
    )
