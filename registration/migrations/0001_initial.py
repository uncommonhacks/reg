# Generated by Django 2.1.1 on 2018-09-06 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_adult', models.BooleanField(default=False)),
                ('school', models.CharField(max_length=200)),
                ('grad_year', models.CharField(choices=[('19', '2019'), ('20', '2020'), ('21', '2021'), ('22', '2022'), ('23', '2023 or Later'), ('or', 'other')], default='or', max_length=2)),
                ('pronouns', models.CharField(max_length=150)),
                ('race', models.CharField(max_length=150)),
                ('hackathons', models.CharField(max_length=150)),
                ('essay1', models.TextField(max_length=1500)),
                ('essay2', models.TextField(max_length=1500)),
                ('essay3', models.TextField(max_length=1500)),
                ('essay4', models.TextField(max_length=1500)),
                ('essay5', models.TextField(max_length=1500)),
                ('proudof', models.TextField(max_length=1500)),
                ('reimbursement', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=200)),
                ('inforelease', models.BooleanField(default=False)),
                ('termsconditions', models.BooleanField(default=False)),
                ('code_of_conduct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=20)),
                ('dietary_restrictions', models.CharField(max_length=1000)),
                ('shirt_size', models.CharField(choices=[('XS', 'XS'), ('S_', 'S'), ('M_', 'M'), ('L_', 'L'), ('1X', 'XL'), ('2X', 'XXL')], default='M_', max_length=2)),
                ('notes', models.TextField(max_length=1500)),
            ],
        ),
        migrations.AddField(
            model_name='applicant',
            name='application',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Application'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='confirmation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.Confirmation'),
        ),
    ]
