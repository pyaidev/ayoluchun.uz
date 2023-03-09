# Generated by Django 4.1.7 on 2023-03-09 10:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('surname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Surname')),
                ('patronymic', models.CharField(blank=True, max_length=50, null=True, verbose_name='Patronymic')),
                ('username', models.CharField(blank=True, max_length=255, unique=True, verbose_name='Phone')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UZ')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('email_is_verified', models.BooleanField(default=False, verbose_name='Email is verified')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_active', models.BooleanField(default=True)),
                ('date_login', models.DateTimeField(auto_now=True, verbose_name='Date login')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Speciality',
                'verbose_name_plural': 'Specialities',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500, verbose_name='Bio')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='Image')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=211, verbose_name='Gender')),
                ('zip_code', models.CharField(blank=True, max_length=30, verbose_name='Zip code')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('workplace', models.CharField(blank=True, max_length=255, verbose_name='Workplace')),
                ('imkon_profile', models.CharField(blank=True, max_length=255, validators=[django.core.validators.RegexValidator(regex=re.compile('^(https?://)?(www\\.)?imkon.uz/(?P<username>[a-zA-Z0-9(\\.\\?)?])+$'))], verbose_name='Imkon profile')),
                ('facebook_profile', models.CharField(blank=True, max_length=255, validators=[django.core.validators.RegexValidator(regex=re.compile('^(https?://)?(www\\.)?facebook.com/(?P<username>[a-zA-Z0-9(\\.\\?)?])+$'))], verbose_name='Facebook profile')),
                ('telegram_profile', models.CharField(blank=True, max_length=255, validators=[django.core.validators.RegexValidator(regex=re.compile('^(https?://)?(www\\.)?telegram.com/(?P<username>[a-zA-Z0-9(\\.\\?)?])+$'))], verbose_name='Telegram profile')),
                ('linkden_profile', models.CharField(blank=True, max_length=255, validators=[django.core.validators.RegexValidator(regex=re.compile('^(https?://)?(www\\.)?linkden.com/(?P<username>[a-zA-Z0-9(\\.\\?)?])+$'))], verbose_name='Linkden profile')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.country', verbose_name='Country')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.region', verbose_name='Region')),
                ('speciality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.speciality', verbose_name='Speciality')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User profile',
                'verbose_name_plural': 'User profiles',
            },
        ),
    ]
