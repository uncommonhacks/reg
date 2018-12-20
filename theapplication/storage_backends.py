from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.AWS_STATIC_LOCATION


def upload_resume_to_s3(resume_file, user):
    s3 = boto3.client('s3')
    s3.upload_fileobj(resume_file, settings.RESUME_BUCKET, user.first_name + '_' + user.last_name + '.pdf')
