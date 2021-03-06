from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    # authentication endpoints
    url(r"^accounts/", include("theapplication.accounts_urls")),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    path("apply/", views.application, name="application"),
    path("confirm/", views.confirmation, name="confirmation"),
    path("", views.index, name="index"),
]
