# Generated by Django 4.0.3 on 2022-04-14 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='des',
            field=models.CharField(default='test', max_length=300),
        ),
    ]
