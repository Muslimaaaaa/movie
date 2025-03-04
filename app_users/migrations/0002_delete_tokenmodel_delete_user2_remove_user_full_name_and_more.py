# Generated by Django 5.1.6 on 2025-02-21 00:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TokenModel',
        ),
        migrations.DeleteModel(
            name='User2',
        ),
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '998900404001'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')]),
        ),
    ]
