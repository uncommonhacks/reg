import datetime

import django

app_deadline_dt = datetime.datetime(2019, 1, 20, hour=23, minute=59, second=59)
con_deadline_dt = datetime.datetime(2019, 1, 27, hour=23, minute=59, second=59)


def over_application_deadline():
    return datetime.datetime.now() >= app_deadline_dt


def over_confirmation_deadline():
    return datetime.datetime.now() >= con_deadline_dt
