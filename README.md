Registration for uncommon hacks.


### AWS SSM Parameter Store Config

set django-registration-url to be the hostname part of the URL that zappa gives you when you run zappa update. Should be of type String.

set registration-django-secret-key (type SecureString) to be the "secret key" from django's settings.py. it should just be a long random string lol
