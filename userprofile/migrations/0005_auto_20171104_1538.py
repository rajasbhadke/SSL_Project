# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-04 15:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_about_us_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_us',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]