from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from django.db.models import Q
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from theapplication.models import Applicant


def send_notification_email(email_addr, first_name):
    context = {"site": settings.MAIN_URL, "first_name": first_name}
    subject = render_to_string(
        template_name="emails/email_blast_subject.txt", context=context
    )
    subject = "".join(subject.splitlines())
    message = render_to_string(
        template_name="emails/email_blast_contents.html", context=context
    )
    plain_message = strip_tags(message)
    from_email = settings.DEFAULT_FROM_EMAIL

    mail.send_mail(
        subject, plain_message, from_email, [email_addr], html_message=message
    )
    print("emailed {}".format(email_addr))


class Command(BaseCommand):
    help = "send email blast to anyone who's accepted but not confirmed"

    def handle(self, *args, **options):
        for a in Applicant.objects.filter(status='AM').all():
            send_notification_email(a.user.email, a.user.first_name)
