Registration for uncommon hacks.

start by asking Claude or Ben to make you an account on the uncommonhacks AWS. Then go to IAM and generate yourself some keys.

to set this up, install `aws-cli` onto your dev machine, then run `aws configure` and put in the key stuff from IAM.

After that you should be good to just run `zappa update` from the main directory and itll push to the dev lambda w00t

### AWS SSM Parameter Store Config

*this is already done on the uncommonhacks aws*

set django-registration-url to be the hostname part of the URL that zappa gives you when you run zappa update. Should be of type String.

set registration-django-secret-key (type SecureString) to be the "secret key" from django's settings.py. it should just be a long random string lol
