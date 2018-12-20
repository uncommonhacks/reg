from django.conf.urls import url
from django.views.generic.base import TemplateView
from registration.backends.default.views import RegistrationView
from . import views

# code taken from django-registration library
urlpatterns = [
    url(
        r"^activate/complete/$",
        TemplateView.as_view(
            template_name="django_registration/activation_complete.html"
        ),
        name="registration_activation_complete",
    ),
    # The activation key can make use of any character from the
    # URL-safe base64 alphabet, plus the colon as a separator.
    url(
        r"^activate/(?P<activation_key>[-:\w]+)/$",
        views.ApplicantActivationView.as_view(),
        name="registration_activate",
    ),
    url(
        r"^register/$",
        RegistrationView.as_view(
            template_name="django_registration/registration_form.html"
        ),
        name="registration_register",
    ),
    url(
        r"^register/complete/$",
        TemplateView.as_view(
            template_name="django_registration/registration_complete.html"
        ),
        name="registration_complete",
    ),
    url(
        r"^register/closed/$",
        TemplateView.as_view(
            template_name="django_registration/registration_closed.html"
        ),
        name="registration_disallowed",
    ),
]
