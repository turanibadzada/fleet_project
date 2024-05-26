# Generated by Django 5.0.3 on 2024-05-25 13:58

import accounts.models
import django_countries.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('surname', models.CharField(blank=True, max_length=250, null=True)),
                ('bio', models.CharField(blank=True, max_length=250, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_to)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_to)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=25, null=True)),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('social', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('activation_code', models.CharField(blank=True, max_length=6, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['-timestamp'],
            },
        ),
    ]
