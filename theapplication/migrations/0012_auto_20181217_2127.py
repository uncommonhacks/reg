# Generated by Django 2.1.3 on 2018-12-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("theapplication", "0011_auto_20181217_2126")]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="race",
            field=models.ManyToManyField(
                to="theapplication.RaceChoice",
                verbose_name="What is your race/ethnicity?",
            ),
        )
    ]
