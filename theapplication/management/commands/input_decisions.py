from theapplication.models import Applicant 
from django.core.management.base import BaseCommand, CommandError

def do_status_routine(emails_file, decision):
    # first, parse the emails_file
    with open(emails_file, 'r') as f:
        emails = f.readlines()
    for email in emails:

        
class Command(BaseCommand):
    help = 'Changes statuses as defined in file'

    def add_arguments(self, parser):
    parser.add_argument('--accept_file', nargs='?', help='filename of newline-separated emails for accounts to accept')
    parser.add_argument('--waitlist_file', nargs='?', help='filename of newline-separated emails for accounts to waitlist')
    parser.add_argument('--reject_file', nargs='?', help='filename of newline-separated emails for accounts to reject')
   
    def handle(self, *args, **options):
        if 'accept_file' in options:
            do_status_routine(options['accept_file'], 'ACCEPT')
        else:
            print('no accept file provided. continuing...')
        if 'waitlist_file' in options:
            do_status_routine(options['waitlist_file'], 'WAITLIST')
        else:
            print('no waitlist file provided. continuing...')
        if 'reject_file' in options:
            do_status_routine(options['reject_file'], 'REJECT')
        else:
            print('no reject file provided. continuing...')
        print('done!')
