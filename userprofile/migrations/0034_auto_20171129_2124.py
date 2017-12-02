# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-29 21:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0033_auto_20171129_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('created', models.DateTimeField()),
                ('webmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_type', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('flag', models.BooleanField(default=False)),
                ('webmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='mail',
            old_name='mailInfo',
            new_name='mail_info',
        ),
    ]
