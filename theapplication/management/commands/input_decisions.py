from theapplication.models import Applicant
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
import sys

def do_status_routine(username_file, decision, mystdout):
    old_stdout = sys.stdout
    sys.stdout = mystdout
    # first, parse the emails_file
    try:
        with open(username_file, 'r') as f:
            usernames = f.readlines()
    except:
        sys.stdout = old_stdout
        raise CommandError('Problem opening username file {}.' % username_file)
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

    for uname in usernames:
        uname = uname.strip()
        try:
            user = User.objects.get(username=uname)
            applicant = Applicant.objects.get(user=user)
        except User.DoesNotExist:
            print('{} does not exist. skipping.'.format(uname))
            continue
        except Applicant.DoesNotExist:
            print('{} does not have an attached Applicant. skipping.'.format(uname))
            continue

        skip = False
        print('Processing {}.'.format(uname))
        if applicant.status == 'NS':
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
        parser.add_argument('--accept_file', nargs='?', help='filename of newline-separated usernames for accounts to accept')
        parser.add_argument('--waitlist_file', nargs='?', help='filename of newline-separated usernames for accounts to waitlist')
        parser.add_argument('--reject_file', nargs='?', help='filename of newline-separated usernames for accounts to reject')
   
    def handle(self, *args, **options):
        if options['accept_file']:
            do_status_routine(options['accept_file'], 'ACCEPT', self.stdout)
        else:
            self.stdout.write('no accept file provided. continuing...')
        if options['waitlist_file']:
            do_status_routine(options['waitlist_file'], 'WAITLIST', self.stdout)
        else:
            self.stdout.write('no waitlist file provided. continuing...')
        if options['reject_file']:
            do_status_routine(options['reject_file'], 'REJECT', self.stdout)
        else:
            self.stdout.write('no reject file provided. continuing...')
