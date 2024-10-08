# Generated by Django 5.0.3 on 2024-08-07 18:32

import ckeditor.fields
import django.db.models.deletion
import mptt.fields
import phonenumber_field.modelfields
import services.uploader
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
            name='Additional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('name_az', models.CharField(max_length=250, null=True)),
                ('name_ru', models.CharField(max_length=250, null=True)),
                ('icon', models.ImageField(upload_to=services.uploader.Uploader.additional_image_uploader)),
            ],
            options={
                'verbose_name': 'Additional',
                'verbose_name_plural': 'Additionals',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('name_az', models.CharField(max_length=250, null=True)),
                ('name_ru', models.CharField(max_length=250, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=services.uploader.Uploader.category_image_uploader)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='houses.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('name_en', models.CharField(max_length=150, null=True)),
                ('name_az', models.CharField(max_length=150, null=True)),
                ('name_ru', models.CharField(max_length=150, null=True)),
                ('living_room', models.IntegerField(choices=[(1, '1 Room'), (2, '2 Rooms'), (3, '3 Rooms'), (4, '4 Rooms and more')])),
                ('bed_room', models.IntegerField(choices=[(1, '1 Room'), (2, '2 Rooms'), (3, '3 Rooms'), (4, '4 Rooms and more')])),
                ('bath_room', models.IntegerField(choices=[(1, '1 Room'), (2, '2 Rooms'), (3, '3 Rooms'), (4, '4 Rooms and more')])),
                ('address', ckeditor.fields.RichTextField()),
                ('discount_interest', models.IntegerField(blank=True, choices=[(10, '10% off'), (15, '15% off'), (20, '20% off'), (25, '25% off'), (200, 'from 200$'), (230, 'from 230$'), (250, 'from 250$'), (300, 'from 300$')], null=True)),
                ('status', models.CharField(choices=[('Featured', 'Featured'), ('Family-friendly', 'Family-friendly'), ('On sale', 'On sale'), ('Sub nav', 'Sub nav')], max_length=250)),
                ('description', ckeditor.fields.RichTextField()),
                ('description_en', ckeditor.fields.RichTextField(null=True)),
                ('description_az', ckeditor.fields.RichTextField(null=True)),
                ('description_ru', ckeditor.fields.RichTextField(null=True)),
                ('price', models.IntegerField()),
                ('location_url', models.URLField(blank=True, null=True)),
                ('people_count', models.IntegerField()),
                ('children', models.IntegerField(default=0)),
                ('amenities', models.ManyToManyField(blank=True, to='houses.additional')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='houses.category')),
                ('hosted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='countries.countries')),
            ],
            options={
                'verbose_name': 'House',
                'verbose_name_plural': 'Houses',
            },
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=services.uploader.Uploader.house_image_uploader)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.house')),
            ],
            options={
                'verbose_name': 'House Image',
                'verbose_name_plural': 'House Images',
            },
        ),
        migrations.CreateModel(
            name='HouseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=250)),
                ('password_series', models.CharField(max_length=250)),
                ('check_in', models.DateTimeField(blank=True, null=True)),
                ('check_out', models.DateTimeField(blank=True, null=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.house')),
                ('payment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.payment')),
            ],
            options={
                'verbose_name': 'House Order',
                'verbose_name_plural': 'House Orders',
            },
        ),
        migrations.CreateModel(
            name='HouseReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rating', models.PositiveIntegerField(choices=[(1, '★✩✩✩✩'), (2, '★★✩✩✩'), (3, '★★★✩✩'), (4, '★★★★✩'), (5, '★★★★★')])),
                ('message', models.TextField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.house')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='houses.housereview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'House Review',
                'verbose_name_plural': 'House Reviews',
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.house')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'List',
                'verbose_name_plural': 'Wishlist',
            },
        ),
    ]
