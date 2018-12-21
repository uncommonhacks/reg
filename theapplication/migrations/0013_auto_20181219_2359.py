# Generated by Django 2.1.3 on 2018-12-19 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("theapplication", "0012_auto_20181217_2127")]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="gender",
            field=models.CharField(
                choices=[
                    ("M_", "Male"),
                    ("NB", "Nonbinary"),
                    ("F_", "Female"),
                    ("or", "Other / Prefer not to disclose"),
                ],
                default="or",
                max_length=2,
            ),
        )
    ]