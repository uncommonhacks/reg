# Generated by Django 2.1.2 on 2019-01-25 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapplication', '0032_auto_20181224_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmation',
            name='over18',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
    ]
