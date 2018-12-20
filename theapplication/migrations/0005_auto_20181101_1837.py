# Generated by Django 2.1.2 on 2018-11-01 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapplication', '0004_application_race_select'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='race_select',
        ),
        migrations.RemoveField(
            model_name='application',
            name='race',
        ),
        migrations.AddField(
            model_name='application',
            name='race',
            field=models.ManyToManyField(to='theapplication.RaceChoice'),
        ),
    ]
