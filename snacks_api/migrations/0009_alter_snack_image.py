# Generated by Django 4.0.4 on 2022-04-22 23:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snacks_api', '0008_merge_20220420_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
