# Generated by Django 2.1.2 on 2018-12-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("theapplication", "0031_auto_20181223_2334")]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="school",
            field=models.CharField(
                help_text='If your school does not appear on the list, select "Other"',
                max_length=200,
                null=True,
                verbose_name="Where do you attend school?",
            ),
        ),
        migrations.DeleteModel(name="SchoolChoice"),
    ]
