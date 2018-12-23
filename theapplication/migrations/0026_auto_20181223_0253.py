# Generated by Django 2.1.2 on 2018-12-23 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapplication', '0025_auto_20181222_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='school',
        ),
        migrations.AddField(
            model_name='application',
            name='school',
            field=models.ForeignKey(help_text='SELECT OTHER', null=True, on_delete='SET_NULL', to='theapplication.SchoolChoice', verbose_name='Where do you attend school? If your school does not appear on the list, select "Other".'),
        ),
    ]