"""
Django settings for reg project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os, boto3

# get boto3 client to initialize other settings
client = boto3.client("ssm")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = client.get_parameter(
    Name="registration-django-secret-key", WithDecryption=True
)["Parameter"]["Value"]

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get("RUN_LOCAL") == "TRUE":
    DEBUG = True
    ALLOWED_HOSTS = ["*"]
else:
    DEBUG = False
    ALLOWED_HOSTS = [
        "127.0.0.1",
        "localhost",
        "bcdeda7b.ngrok.io",
        MAIN_URL,
        client.get_parameter(Name="django-registration-url")["Parameter"]["Value"],
    ]


DEBUG = True
MAIN_URL = "testing.uncommonhacks.com"


# Application definition

INSTALLED_APPS = [
    "theapplication.apps.TheapplicationConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.forms",
    "phonenumber_field",
    "registration",
    "storages",
    "anymail",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "reg.urls"

DEFAULT_CHARSET = "utf-8"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["./templates", "django/forms/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "reg.wsgi.application"


# email
ANYMAIL = {"MAILGUN_API_KEY": client.get_parameter(Name="MAILGUN_API_KEY", WithDecryption=True)["Parameter"]["Value"]}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@uncommonhacks.com"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if os.environ.get("RUN_LOCAL") == "TRUE":
    DB_NAME = "ucreg"
    DB_USER = "ucreguser"
    DB_PASS = "usregpassword"
    DB_HOST = "localhost"
    DB_PORT = ""
else:
    DB_NAME = client.get_parameter(Name="db_name")["Parameter"]["Value"]
    DB_USER = client.get_parameter(Name="db_user")["Parameter"]["Value"]
    DB_PASS = client.get_parameter(Name="db_pass", WithDecryption=True)["Parameter"][
        "Value"
    ]
    DB_HOST = client.get_parameter(Name="db_host")["Parameter"]["Value"]
    DB_PORT = 5432


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASS,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "accounts/login/"
ACCOUNT_ACTIVATION_DAYS = 7

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

if os.environ.get("RUN_LOCAL") == "TRUE":
    STATIC_ROOT = "static"
    STATIC_URL = "/static/"
    AWS_STATIC_LOCATION = "static"
else:
    AWS_STORAGE_BUCKET_NAME = client.get_parameter(Name="static_bucket")["Parameter"][
        "Value"
    ]

    AWS_S3_CUSTOM_DOMAIN = "%s.s3.us-east-2.amazonaws.com" % AWS_STORAGE_BUCKET_NAME

    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

    AWS_STATIC_LOCATION = "static"
    STATICFILES_STORAGE = "theapplication.storage_backends.StaticStorage"
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
    AWS_DEFAULT_ACL = 'public-read'
RESUME_BUCKET = client.get_parameter(Name="resume_bucket")["Parameter"]["Value"]


FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

PHONENUMBER_DB_FORMAT = "E164"
