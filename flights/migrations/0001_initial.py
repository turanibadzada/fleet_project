# Generated by Django 5.0.3 on 2024-05-25 13:58

import ckeditor.fields
import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('countries', '0001_initial'),
        ('payment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('name_az', models.CharField(max_length=250, null=True)),
                ('name_ru', models.CharField(max_length=250, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('description_en', ckeditor.fields.RichTextField(null=True)),
                ('description_az', ckeditor.fields.RichTextField(null=True)),
                ('description_ru', ckeditor.fields.RichTextField(null=True)),
                ('image', models.ImageField(upload_to='photo/')),
                ('company_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='countries.countries')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='TicketSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('departure_time', models.DateTimeField()),
                ('arrivel_time', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('parking_areas', models.CharField(choices=[('Nonstop', 'Nonstop'), ('1 Stop', '1 Stop'), ('2+ Stop', '2+ Stop')], max_length=100)),
                ('class_of_services', models.CharField(choices=[('economy', 'Economy'), ('comfort', 'Comfort'), ('business', 'Business'), ('first', 'First')], max_length=100)),
                ('people_count', models.IntegerField()),
                ('children_count', models.IntegerField(default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.company')),
                ('departure_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deptarture_country', to='countries.countries')),
                ('destination_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.countries')),
            ],
            options={
                'verbose_name_plural': 'TicketSales',
            },
        ),
        migrations.CreateModel(
            name='TicketOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Canceled', 'Canceled'), ('Approved', 'Approved')], max_length=250)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=250)),
                ('password_series', models.CharField(max_length=250)),
                ('seat_number', models.CharField(max_length=250)),
                ('payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
                ('ticket_sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.ticketsales')),
            ],
            options={
                'verbose_name': 'Ticket Order',
                'verbose_name_plural': 'Ticket Orders',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ticketsales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.ticketsales')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userr', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'List',
                'verbose_name_plural': 'Wishlist',
            },
        ),
    ]
