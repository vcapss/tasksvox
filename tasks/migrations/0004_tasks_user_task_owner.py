# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 00:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_tasks_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='user_task_owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
