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
        template_name="emails/decision_email_subject.txt", context=context
    )
    subject = "".join(subject.splitlines())
    message = render_to_string(
        template_name="emails/decision_email_contents.html", context=context
    )
    plain_message = strip_tags(message)
    from_email = settings.DEFAULT_FROM_EMAIL
    mail.send_mail(
        subject, plain_message, from_email, [email_addr], html_message=message
    )
    print("emailed {}".format(email_addr))


class Command(BaseCommand):
    help = "Emails set group of users their status, or emails all users that are accepted/waitlisted/rejected and have the notified_of_admit_status flag set to false."

    def add_arguments(self, parser):
        parser.add_argument(
            "--force-username-file",
            nargs="?",
            help="instead of emailing everyone with a decision who hasn't been notified, email everyone on the list with their current status.",
        )

    def handle(self, *args, **options):
        if options["force_username_file"]:
            with open(options["force_username_file"]) as f:
                unames = f.readlines()
            for uname in unames:
                try:
                    uname = uname.strip()
                    user = User.objects.get(username=uname)
                    send_notification_email(user.email, user.first_name)
                except Exception as e:
                    self.stdout.write("failed to email user {}".format(uname))
        else:
            not_admit = Q(status="NA")
            admit = Q(status="AM")
            waitlist = Q(status="WA")
            not_notified = Q(notified_of_admit_status=False)
            queryset = Applicant.objects.all().filter(
                not_notified, not_admit | admit | waitlist
            )
            for applicant in queryset:
                try:
                    user = applicant.user
                    send_notification_email(user.email, user.first_name)
                    applicant.notified_of_admit_status = True
                    applicant.save()
                except:
                    self.stdout.write("failed to email user {}".format(user.username))
