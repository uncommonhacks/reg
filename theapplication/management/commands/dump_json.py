from theapplication.models import Applicant, Application, Confirmation
from django.core.management.base import BaseCommand
import json
from pathlib import Path

def get_data_from_confirmation(confirmation):
    if not confirmation:
        return None
    conf_data = {}
    conf_data['dietary_restrictions'] = confirmation.dietary_restrictions
    conf_data['shirt_size'] = confirmation.shirt_size
    conf_data['notes'] = confirmation.notes
    return conf_data

def get_data_from_application(application):
    if not application:
        return None
    app_data = {}
    app_data['phone_number'] = application.phone_number
    app_data['birth_date'] = str(application.birth_date)
    app_data['gender'] = application.gender
    app_data['pronouns'] = application.pronouns
    app_data['race'] = list(map(str, list(application.race.all())))
    app_data['school'] = application.school
    app_data['study_level'] = application.study_level
    app_data['grad_year'] = application.grad_year
    app_data['location'] = application.location
    app_data['hackathons'] = application.hackathons
    app_data['self_description'] = application.self_description
    app_data['proudof'] = application.proudof
    app_data['essay1'] = application.essay1
    app_data['essay2'] = application.essay2
    app_data['essay3'] = application.essay3
    app_data['legal1'] = application.legal1
    app_data['legal2'] = application.legal2
    app_data['legal3'] = application.legal3
    app_data['brain_1'] = application.brain_1
    app_data['brain_2'] = application.brain_2
    app_data['brain_3'] = application.brain_3
    app_data['brain_4'] = application.brain_4
    app_data['is_this_a_1'] = application.is_this_a_1
    app_data['is_this_a_2'] = application.is_this_a_2
    app_data['is_this_a_3'] = application.is_this_a_3
    app_data['pikachu'] = application.pikachu
    return app_data

def get_data_from_applicant(applicant):
    if not applicant:
        return None
    app_data = {}
    app_data['username'] = applicant.user.username
    app_data['first_name'] = applicant.user.first_name
    app_data['last_name'] = applicant.user.last_name
    app_data['email'] = applicant.user.email
    app_data['status'] = applicant.status
    app_data['notified_of_admit_status'] = applicant.notified_of_admit_status
    app_data['application'] = get_data_from_application(applicant.application)
    app_data['confirmation'] = get_data_from_confirmation(applicant.confirmation)
    return app_data

class Command(BaseCommand):
    help = "Dumps all application data to provided path. relative to $HOME."

    def add_arguments(self, parser):
        parser.add_argument('outfile',
            help="file to dump json output to",
        )

    def handle(self, *args, **options):
        db_data = [get_data_from_applicant(a) for a in Applicant.objects.all()]
        
        with open(str(Path.home()) + '/' + options['outfile'], 'w') as f:
            f.write(json.dumps(db_data, indent=4, separators=(',', ': ')))
        
        self.stdout.write('wrote db dump to: ' + options['outfile'])
