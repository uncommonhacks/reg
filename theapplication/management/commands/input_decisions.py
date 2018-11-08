from theapplication.models import Applicant
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
import sys

def do_status_routine(emails_file, decision, mystdout):
    old_stdout = sys.stdout
    sys.stdout = mystdout
    # first, parse the emails_file
    try:
        with open(emails_file, 'r') as f:
            emails = f.readlines()
    except:
        sys.stdout = old_stdout
        raise CommandError('Problem opening email file {}.' % emails_file)
        return

    if decision == 'ACCEPT':
        new_status = 'AM'
    elif decision == 'REJECT':
        new_status = 'NA'
    elif decision == 'WAITLIST':
        new_status = 'WA'
    else:
        sys.stdout = old_stdout
        raise CommandError('Invalid decision code {}.' % decision)
        return

    for email in emails:
        email = email.strip()
        try:
            user = User.objects.get(email=email)
            applicant = Applicant.objects.get(user=user)
        except User.DoesNotExist:
            print('{} does not exist. skipping.'.format(email))
            continue
        except Applicant.DoesNotExist:
            print('{} does not have an attached Applicant. skipping.'.format(email))
            continue

        skip = False
        if applicant.status in ['NS', 'IP']:
            skip = get_skip_confirmation('Applicant has not finished application. Are you sure you want to make a decision?')
        elif applicant.status == 'CF':
            skip = get_skip_confirmation('Applicant is confirmed already. Are you sure you want to change their status?')
        elif applicant.status == new_status and applicant.notified_of_admit_status:
            skip = get_skip_confirmation('Applicant already has this status and has been notified. Mark for re-notification?')
        if skip:
            continue
        applicant.status = new_status
        applicant.notified_of_admit_status = False
        applicant.save()
    sys.stdout = old_stdout

def get_skip_confirmation(message):
    while True:
        response = input(message + ' [y/n]')
        if response == 'y':
            return False
        elif response == 'n':
            return True


class Command(BaseCommand):
    help = 'Changes statuses as defined in file'

    def add_arguments(self, parser):
        parser.add_argument('--accept_file', nargs='?', help='filename of newline-separated emails for accounts to accept')
        parser.add_argument('--waitlist_file', nargs='?', help='filename of newline-separated emails for accounts to waitlist')
        parser.add_argument('--reject_file', nargs='?', help='filename of newline-separated emails for accounts to reject')
   
    def handle(self, *args, **options):
        if 'accept_file' in options:
            do_status_routine(options['accept_file'], 'ACCEPT', self.stdout)
        else:
            self.stdout.write('no accept file provided. continuing...')
        if 'waitlist_file' in options:
            do_status_routine(options['waitlist_file'], 'WAITLIST', self.stdout)
        else:
            self.stdout.write('no waitlist file provided. continuing...')
        if 'reject_file' in options:
            do_status_routine(options['reject_file'], 'REJECT', self.stdout)
        else:
            self.stdout.write('no reject file provided. continuing...')
