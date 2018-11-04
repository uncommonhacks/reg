import datetime

application_deadline = '12:00:00 11/08/2018' # 'HH:mm:ss MM/DD/YYYY' format
confirmation_deadline = '12:00:00 11/16/2018'

format_str = '%H:%M:%S %m/%d/%Y'
app_deadline_dt = datetime.strptime(application_deadline, format_str)
con_deadline_dt = datetime.strptime(confirmation_deadline, format_str)

def over_application_deadline():
    return datetime.now() >= app_deadline_dt

def over_confirmation_deadline():
    return datetime.now() >= con_deadline_dt


